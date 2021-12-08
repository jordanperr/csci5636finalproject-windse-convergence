import windse_driver.driver_functions as df
import yaml
import pandas as pd
import glob


def run():
    experiment_name = "2d-n"
    params_dict = yaml.safe_load(open("convergence-2D-3-Turbine.yaml"))
    results = []

    for nx in range(110,200+1,10):

        params_dict["domain"]["nx"] = nx
        params_dict["domain"]["ny"] = nx
        params_dict["general"]["name"] = f"{experiment_name}{nx}"

        params, problem, solver = df.SetupSimulation(params_dict)

        solver.Solve()

        results.append({"params":params, "problem":problem, "solver":solver})

    #pickle.dump(results, open(f"./output/{experiment_name}.results.pickle","wb"))

def load_power(path):
    df = pd.read_csv(path, header=None, skiprows=[0], sep=" ")
    df.columns = ["time", "Turbine 1", "Turbine 2", "Turbine 3", "sum"]
    return df

def load_result(path):
    df = load_power(path+"/data/2d_power_data.txt")
    df["path"] = path
    df["logfile"] = open(path+"/log.txt","r").read()
    df["dofs"] = df["logfile"].str.extract("Total DOFS: +(\d+)").astype("int")
    df["nx"] = df["path"].str.extract(r'-n(\d+)').astype("int")
    return df

def get_results():
    df = pd.concat(map(load_result, glob.glob("./output/2d-n*"))).sort_values("nx")
    return df

if __name__=="__main__":
    run()