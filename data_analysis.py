"""
__filename__ = "data_analysis.py"
__author__ = "Elias Hong"
__copyright__ = "None"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Elias Hong"
__email__ = "eliash0913@gmail.com"
__status__ = "Completed"
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
class Data:
    """
    data class to load data_set and access to the column.
    """
    file_name = "No File opened"
    data_set = pd
    def __init__(self, file_name, header_line=None, index_column=None):
        """
        data class constructor
        """
        self.file_name = file_name
        self.data_set = pd.read_csv(file_name, header=header_line, sep=',', index_col=index_column)

    def get(self, column_name=None):
        """
        get method to get column data set. if column name is not specified,
        return whole data set.
        """
        if column_name is None:
            data_column_set = self.data_set
        else:
            data_column_set = DataColumn(column_name, self.data_set[column_name])
        return data_column_set

class DataColumn():
    """
    data_column class for data column set
    to load data_set and access to the column.
    """
    data_array = np
    column_name = ""
    def __init__(self, column_name, data_column_set):
        """
        data_column class constructor
        """
        self.column_name = column_name
        self.data_array = np.nan_to_num(np.array(data_column_set))

    def get(self):
        """
        get method to return column data set.
        """
        return self.data_array

    def mean(self):
        """
        mean method to return mean value of the column data set.
        """
        return np.mean(self.data_array)

    def std(self):
        """
        std method to return standard deviation value of the column data set.
        """
        return np.std(self.data_array)

    def min(self):
        """
        min method to return min value of the column data set.
        """
        return np.min(self.data_array)

    def max(self):
        """
        max method to return mean value of the column data set.
        """
        return np.max(self.data_array)

    def count(self):
        """
        count method to return count value of the column data set.
        """
        return self.data_array.size

    def hist(self):
        """
        hist method to generate histogram of column and save as the column name.
        """
        plt.hist(self.data_array, bins='auto', density=False, facecolor='b')
        plt.title(self.column_name)
        plt.savefig(self.column_name + ".svg")
        plt.close()

def main():
    print("MAIN CODE")

def get_statistics(column_data):
    """
    get_statistics(column) to take data column and calculate,
    display statistics, and save histogram.
    """
    print("The statistics for this column are:")
    print("Count = ", column_data.count())
    print("Mean = ", column_data.mean())
    print("Standard Deviation = ", column_data.std())
    print("Min = ", column_data.min())
    print("Max = ", column_data.max())
    column_data.hist()
    print("The Histogram of this column can be downloaded now.")

if __name__ == "__main__":
    main()
