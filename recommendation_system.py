# Create a dictionary with movies and their genres
movies = {
    "The Matrix": "Sci-Fi",
    "The Godfather": "Drama",
    "Toy Story": "Animation",
    "Inception": "Sci-Fi",
    "Titanic": "Romance",
    "The Dark Knight": "Action",
    "Forrest Gump": "Drama"
}

# Create a dictionary with user ratings for movies
user_ratings = {
    "Alice": {"The Matrix": 5, "Inception": 4, "Titanic": 3},
    "Bob": {"The Godfather": 5, "The Dark Knight": 4, "Forrest Gump": 5},
    "Charlie": {"Toy Story": 5, "The Matrix": 3, "Inception": 5}
}

# Function to recommend movies by genre
def recommend_by_genre(genre):
    recommendations = []
    for movie, movie_genre in movies.items():
        if movie_genre.lower() == genre.lower():
            recommendations.append(movie)
    return recommendations

# Function to find similar users based on common movie ratings
def find_similar_users(target_user, user_ratings):
    similarities = {}
    for user, ratings in user_ratings.items():
        if user != target_user:
            common_movies = set(user_ratings[target_user].keys()) & set(ratings.keys())
            if common_movies:
                similarity = sum(user_ratings[target_user][movie] * ratings[movie] for movie in common_movies)
                similarities[user] = similarity
    return similarities

# Main function to get personalized recommendations for a user
def get_recommendations(username, user_ratings, movies):
    if username not in user_ratings:
        return f"User {username} not found"
    
    similar_users = find_similar_users(username, user_ratings)
    if not similar_users:
        return "No similar users found"
    
    most_similar = max(similar_users, key=similar_users.get)
    
    recommendations = []
    for movie in movies:
        if movie not in user_ratings[username]:
            if movie in user_ratings[most_similar] and user_ratings[most_similar][movie] >= 4:
                recommendations.append(movie)
    
    return recommendations

# Example usage: show recommendations for a user
if __name__ == "__main__":
    print("Movies available:", list(movies.keys()))
    print("\nRecommendations for Alice:", get_recommendations("Alice", user_ratings, movies))
    print("Recommendations for Bob:", get_recommendations("Bob", user_ratings, movies))
    print("\nSci-Fi movies:", recommend_by_genre("Sci-Fi"))