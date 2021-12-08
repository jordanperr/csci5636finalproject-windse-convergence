import windse_driver.driver_functions as df
import yaml
import pandas as pd
import glob

import numpy as np


def run():
    experiment_name = "exp2"
    params_dict = yaml.safe_load(open("convergence-2D-3-Turbine.yaml"))

    for nx in range(60,200+1,20):
        
        for inflow_angle in [0, np.pi/16]:

            for problem_type in ["taylor_hood"]:

                params_dict["general"]["name"] = f"{experiment_name}_nx{nx}_inflow{inflow_angle:.2f}_prob{problem_type}"
                print(params_dict["general"]["name"])

                params_dict["domain"]["nx"] = nx
                params_dict["domain"]["ny"] = nx

                params_dict["boundary_conditions"]["inflow_angle"] = inflow_angle

                params_dict["function_space"]["type"] = problem_type
                params_dict["problem"]["type"] = "stabilized" if problem_type=="linear" else "taylor_hood"

                params, problem, solver = df.SetupSimulation(params_dict)

                solver.Solve()

def load_power(path):
    df = pd.read_csv(path, header=None, skiprows=[0], sep=" ")
    df.columns = ["time", "Turbine 1", "Turbine 2", "Turbine 3", "sum"]
    return df

def load_result(path):
    df = load_power(path+"/data/2d_power_data.txt")
    df["path"] = path
    df["logfile"] = open(path+"/log.txt","r").read()
    df["dofs"] = df["logfile"].str.extract("Total DOFS: +(\d+)").astype("int")
    df["nx"] = df["path"].str.extract(r'_nx(\d+)').astype("int")
    df["inflow"] = df["path"].str.extract(r'_inflow([\d.]+)').astype("float")
    df["problem"] = df["path"].str.extract(r'_prob([\w_]+)').astype("str")
    return df

def get_results():
    df = pd.concat(map(load_result, glob.glob("./output/exp2_*"))).sort_values("nx")
    return df.reset_index()

if __name__=="__main__":
    run()