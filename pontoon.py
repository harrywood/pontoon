import csv

#----------------------------------------------------------------------
def csv_dict_writer(path, fieldnames, data):
    """
    Writes a CSV file using DictWriterpython
    """
    with open(path, 'w') as out_file:
        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
#----------------------------------------------------------------------

if __name__ == "__main__":

    score_dist = [0] * 70
    scores = [0] * 49
    temp_str = ""
    lines_complete = 0

    reader = csv.DictReader(open("comp_scores.csv"), delimiter=',')

    for i in range(1,71):
        temp_str += str(i) + ","
    temp_str = temp_str[:-1]
    data = [temp_str.split(",")]

    for line in reader:
        for a in range(0,49):
            str = "{}".format(a+1)
            scores[a] = int(line[str])

        for a in range(0,43):
            for b in range(a+1,44):
                for c in range(b+1,45):
                    for d in range(c+1,46):
                        for e in range(d+1,47):
                            for f in range(e+1,48):
                                for g in range(f+1,49):
                                    total_score = scores[a]+scores[b]+scores[c]+scores[d]+scores[e]+scores[f]+scores[g]
                                    score_dist[total_score] += 1
                                    # print(score_dist[total_score])

        temp_str = ""
        for h in range(0,70):
            temp_str = temp_str + "{},".format(score_dist[h])
            score_dist[h] = 0
        temp_str = temp_str[:-1]
        
        data.append(temp_str.split(","))
        
        total_score=0;

        lines_complete +=1
        print(lines_complete, "competition(s) calculated")

    my_list = []
    fieldnames = data[0]

    for values in data[1:]:
        inner_dict = dict(zip(fieldnames, values))
        my_list.append(inner_dict)
    path = "score_dist.csv"

    csv_dict_writer(path, fieldnames, my_list)
