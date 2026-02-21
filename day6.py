n=int(input("Enter number of songs: "))
durations=[0]*n
for i in range(n):
    durations[i]=int(input())

invalid=False
for d in durations:
    if d <= 0:
        invalid=True
        break
if invalid:
    print("Invalid Playlist: Contains non-positive duration.")
else:
    total_duration = sum(durations)
    number_of_songs = len(durations)

    if total_duration < 300:
        category="Too short Playlist"
        recommendation="Add more Songs"
    elif total_duration > 3600:
        category="Too long Playlist"
        recommendation="Consider shortening the playlist"
    else:
        repetitive=False
        for d in durations:
            if durations.count(d) > 1:
                repetitive=True
                break
        if repetitive:
            category="Repetitive Playlist"
            recommendation="Add variety"
        else:
            variation=max(durations)-min(durations)
            if variation <=300:
                category="Balanced playlist"
                recommendation="Good listening session"
            else:
                category="Irregular playlist"
                recommendation="Consider having better durations"
    print("Total duration: ",total_duration," seconds")
    print("Number of songs: ",number_of_songs)
    print("Category: ",category)
    print("Recommendation: ",recommendation)