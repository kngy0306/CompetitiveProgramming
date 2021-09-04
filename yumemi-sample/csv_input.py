import csv

MAX_RANK = 10

data = {}


def createUserData(row):
    if row[1] in data:
        player_status = data[row[1]]
        player_status["sum"] += int(row[2])
        player_status["count"] += 1
    else:
        data[row[1]] = {"sum": 0, "count": 0}
        player_status = data[row[1]]
        player_status["sum"] = int(row[2])
        player_status["count"] = 1


def sortUserData(data):
    outputData = {}

    for d in data:
        player_data = data[d]
        mean = int(abs(player_data["sum"] / player_data["count"]))
        outputData[d] = mean

    sort_data = sorted(outputData.items(), key=lambda x: x[1], reverse=True)
    return sort_data


def output(data):
    print("rank,player_id,mean_score")

    rank = 1
    cnt = 1
    pre_score = 0
    for d in data:
      if pre_score == d[1]:
        print(f"{rank},{d[0]},{d[1]}")
        cnt += 1
        pre_score = d[1]
      else:
        if cnt > MAX_RANK:
          break
        rank = cnt
        print(f"{rank},{d[0]},{d[1]}")
        cnt += 1
        pre_score = d[1]


with open("./input.CSV", encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)

    header_checkflag = True
    for row in csvreader:
        # headerの検証
        if header_checkflag:
            if row[0] != 'create_timestamp' or row[1] != 'player_id' or row[2] != 'score':
                print("header is invalid.")
                exit()
            header_checkflag = False
            continue

        createUserData(row)
    ans = sortUserData(data)

output(ans)
