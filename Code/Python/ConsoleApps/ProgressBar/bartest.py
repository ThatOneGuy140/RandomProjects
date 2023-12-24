import ProgressBar as pb

var = 0

while True:
    pb.bar(var,1)
    var += 1

    pb.clear()

    if var >= 11:
        var = 0
    
