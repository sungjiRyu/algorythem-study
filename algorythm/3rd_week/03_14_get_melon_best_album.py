def get_melon_best_album(genre_array, play_array):

    # key : genre, value : play
    genre_total_dict = {}
    # key : genre, value : [index, play]
    genre_index_play_array_dict = {}

    for i in range(len(genre_array)):
        if genre_array[i] in genre_total_dict:
            genre_total_dict[genre_array[i]] += play_array[i]
            genre_index_play_array_dict[genre_array[i]].append([i, play_array[i]])
        else:
            genre_total_dict[genre_array[i]] = play_array[i]
            genre_index_play_array_dict[genre_array[i]] = [[i, play_array[i]]]

    # 가장 재생횟수가 많은 장르
    sorted_genre_play_array = sorted(genre_total_dict.items(), key=lambda item: item[1], reverse=True)

    result = []
    for genre, total_play in sorted_genre_play_array:
        sorted_genre_index_play_array = sorted(genre_index_play_array_dict[genre], key=lambda item: item[1], reverse=True)

        genre_song_count = 0
        for index, play in sorted_genre_index_play_array:
            if genre_song_count >= 2:
                break;

            result.append(index)
            genre_song_count += 1

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))