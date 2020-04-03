#!/bin/bash

sudo sudo -V &> /dev/null

if dot -V &> /dev/null
then
        echo "graphviz already installed"
else
        echo "installing graphviz"
        sudo apt install -y graphviz
fi

if which python3 > /dev/null
then
                echo "python3 already installed"
else
                echo "Installing Python3.7"
                yes | sudo apt install python3.7
fi

if which pip3 > /dev/null
then
                echo "pip3 is alredy installed"
else
                echo "Installing pip3"
                yes | sudo apt install python3-pip
fi

if python3 -c "import sklearn" &> /dev/null
then
        echo "sklearn already installed"
else
        echo "installing sklearn"
        yes | pip3 install scikit-learn
fi

if python3 -c "import pandas" &> /dev/null
then
        echo "pandas already installed"
else
        echo "installing pandas"
        yes | pip3 install pandas
fi

if python3 -c "import matplotlib" &> /dev/null
then
        echo "matplotlib already installed"
else
        echo "installing matplotlib"
        yes | pip3 install matplotlib
fi
