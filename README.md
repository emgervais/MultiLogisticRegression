<body>
    <h1>Data Science Project: Logistic Regression</h1>
    
    <h2>Overview</h2>
    <p>This project aims to implement a logistic regression model using gradient descent for multi-class classification. The project is divided into several parts: data analysis, data visualization, and logistic regression. Each part includes specific tasks to explore, visualize, and model the data without using pre-built functions that simplify the process.</p>
    
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#general-instructions">General Instructions</a></li>
            <ul>
                <li><a href="#data-analysis">Data Analysis</a></li>
                <li><a href="#data-visualization">Data Visualization</a></li>
                <li><a href="#logistic-regression">Logistic Regression</a></li>
            </ul>
        <li><a href="#setup-and-usage">Setup and Usage</a></li>
        <li><a href="#license">License</a></li>
    </ul>
    
    <h2 id="general-instructions">General Instructions</h2>
    <p>We cuold use any programming language you prefer. I chose Python as I already know how to u se the matplotlib library for visualization. Avoid using any pre-built functions that do the heavy-lifting for you (e.g., Pandas <code>describe</code> function). Avoid using functions like <code>count</code>, <code>mean</code>, <code>std</code>, <code>min</code>, <code>max</code>, <code>percentile</code>, etc., from any library.</p>
    
    <h3 id="data-analysis">Data Analysis</h3>
    <p>Perform basic data exploration to understand the dataset. Analyze the data format, types, and ranges.</p>
    <p><strong>Task</strong>: Create a program called <code>describe.[extension]</code> that takes a dataset as a parameter and displays information for all numerical features. Example output:</p>
    <pre>
$> describe.[extension] dataset_train.csv
Feature 1  Feature 2  Feature 3  Feature 4
Count      149.000000 149.000000 149.000000 149.000000
Mean       5.848322   3.051007   3.774497   1.205369
Std        5.906338   3.081445   4.162021   1.424286
Min        4.300000   2.000000   1.000000   0.100000
25%        5.100000   2.800000   1.600000   0.300000
50%        5.800000   3.000000   4.400000   1.300000
75%        6.400000   3.300000   5.100000   1.800000
Max        7.900000   4.400000   6.900000   2.500000
    </pre>
    
    <h3 id="data-visualization">Data Visualization</h3>
    <p>Use visualization tools to gain insights and detect anomalies in the data.</p>
    
    <h4>Histogram</h4>
    <p>Create a script called <code>histogram.[extension]</code> to display a histogram answering the question: Which Hogwarts course has a homogeneous score distribution between all four houses?</p>
    
    <h4>Scatter Plot</h4>
    <p>Create a script called <code>scatter_plot.[extension]</code> to display a scatter plot answering the question: What are the two features that are similar?</p>
    
    <h4>Pair Plot</h4>
    <p>Create a script called <code>pair_plot.[extension]</code> to display a pair plot or scatter plot matrix. Use this visualization to determine which features to use for your logistic regression.</p>
    
    <h3 id="logistic-regression">Logistic Regression</h3>
    <p>Develop a multi-classifier using logistic regression (one-vs-all) with gradient descent to minimize error.</p>
    
    <h4>Training</h4>
    <p>Create a program called <code>logreg_train.[extension]</code> that takes <code>dataset_train.csv</code> as a parameter. This program trains the model and generates a file containing the weights.</p>
    
    <h4>Prediction</h4>
    <p>Create a program called <code>logreg_predict.[extension]</code> that takes <code>dataset_test.csv</code> and the trained weights file as parameters to make predictions.</p>
    
    <h2 id="setup-and-usage">Setup and Usage</h2>
    <ol>
        <li>Clone the repository:
            <pre>git clone https://github.com/yourusername/your-repo-name.git</pre>
        </li>
        <li>Navigate to the project directory:
            <pre>cd your-repo-name</pre>
        </li>
        <li>run the ./script to install all requirements then actiavte you virtual environement</li>
        <li>Follow the instructions in each section to run the scripts for data analysis, visualization, and logistic regression.</li>
    </ol>
    
    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p
</body>
