Python code for data validation and feasibility map  

Draft and run the python code for data validation against COMSOL results from Jim. 

Code Repository: git@github.com:kelsrepo/TEC_model.git 

Steps: 

Got .csv file from Jim 

Ran the code in Code Repository in GitHub 

Ran test.py for test run 

Run main.py 

This will print the first few rows and summary statistics, and save the full table to results/feasibility_sweep.csv 

Run plot_results.py 

This will plot a visual contour plot showing where COP is highest/lowest across current and ΔT 

Run validate_against_comsol.py 

All 20 errors should be small (~1-3%, consistent with what you saw at your first test point). If any are large, that flags an interpolation issue worth investigating before trusting the sweep. 

Get the results as shown in Result section 

Note: 

From the results: The system-side lumped energy balance reproduces the COMSOL device-level Qh to within 1% across the tested operating range, confirming the coupling assumption (Qh = Qc + Ptec) is valid for this application. 
