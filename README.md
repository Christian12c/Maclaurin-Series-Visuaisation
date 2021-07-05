# Maclaurin Series Visuaisation

The project was created to visualise how the addition of higher order Maclaurin series terms gives better and better approximations to the original function.


How to use the Visualisation:


When the executable file is run, the following prompt will come up: " Enter the Maclaurin Series function as shown in README.md: ". To generate the graphs, the following input has to be entered: MaclaurinSeries(f(x), n, a, b) where f(x) is the funtion that is to be graphed, n is the highest power the approximations should reach and a and b form an arithmetic sequence, ax + b. 

As successive terms of some Maclaurin series are the same, we can specify an arithmetic sequence that selects the graphs that are to be plotted. Sin(x) for example is an odd function so it only has non-zero coefficients for odd powers and therefore the graph up to the 2n th power is the same as the graph up to the 2n-1 th power. In this case, by setting a = 2 and b = 1, we get odd powered approximations with no two being the same.


For example, if we typed in "MaclaurinSeries(sin(x), 10, 2, 1)" and pressed "Enter", 
