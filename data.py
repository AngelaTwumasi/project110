import statistics

f = pd.read_csv("medium_data.csv")
data = df['id','url','title','subtitle','image','claps','responses','reading_time','publication','date'].tolist()
 
 population_mean = statistics.mean(data)
 print("Population Mean:",population_mean)

 std_deviation = statistics.stdev(data)
print("Satndard Deviation:",std_deviation)

fig = ff.create_distplot([data],['id','url','title','subtitle','image','claps','responses','reading_time','publication','date'],show_hist=False)
fig.show()

dataset = []
for i in range(0, 100):
    random_index= random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)

mean = statistics.mean(dataset)
std_deviation1 = statistics.stdev(dataset)

print("Mean of sample:- ",mean)
print("std_deviation of sample:- ",std_deviation1)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

  mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup()

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ['id','url','title','subtitle','image','claps','responses','reading_time','publication','date'], show_hist=False)
    fig.show()
