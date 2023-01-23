# This class will generate a file that can be used by an agent to learn volume patterns.
# The algorithm used is as follows:
# it will go through the data using a sliding window. The size of the sliding window is sentence + future lookup length
# if in any window, all the entry points have volume data, then it will add this data to a dataframe
# this mechanism is very similar with the gather_history function from data_aggregator.py [it is a good idea to somehow
# use the same function once it does that, then it merges this data based on the index with the action and reward
# column of the data generated by the data_aggregator.py this will create a table like this:
# previous n bars' volume | action | reward
# the index of this data is a datetime object which represent the current row date and all other columns are volume
# data from the previous n bars.
# this information can be given to the learing agent to learn the volume pattern
# todo: complete the implementation

class GenerateVolumeData:
    # def __init__(self):

    def generate_volume_data(self, data_source):
        return 'One day watson, one day!'