from collections import Counter, defaultdict

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"), (6, "probability"),
    (6, "mathematics"), (6, "theory"), (7, "machine learning"), (7, "scikit-learn"),
    (7, "Mahout"), (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
                    (3, 4), (4, 5), (5, 6), (5, 7), (6, 8),
                    (7, 8), (8, 9)]

friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    """QUANTOS AMIGOS TEM O USUÁRIO?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]

    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

print(f"\nMédia de conexões por usuário: {avg_connections}")

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

print("\nNúmero de amigos por usuário (do maior para o menor):")
for user_id, num_friends in num_friends_by_id:
    print(f"Usuário {user_id} tem {num_friends} amigos")

def foaf_ids_bad(user):
    """AMIGOS DE AMIGOS (VERSÃO RUIM)"""
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

print("\nAmigos de amigos (versão ruim) para o usuário 0:")
print(foaf_ids_bad(users[0]))

def friends_of_friends(user):
    """AMIGOS DE AMIGOS (VERSÃO EFICIENTE)"""
    user_id = user["id"]

    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id]
    )

print("\nAmigos de amigos (versão eficiente) para o usuário 0:")
print(friends_of_friends(users[0]))

def data_scientists_who_like(target_interest):
    """ENCONTRAR CIENTISTAS DE DADOS COM INTERESSES SEMELHANTES"""
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interest_by_user_ids = defaultdict(list)
for user_id, interest in interests:
    interest_by_user_ids[user_id].append(interest)


def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interest_by_user_ids[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

print("\nInteresses mais comuns com o usuário 0:")
print(most_common_interests_with(users[0]))

# SALÁRIOS E EXPERIÊNCIA

salaries_and_tenures = [
    (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6),
    (69000, 6.5), (76000, 7.5), (60000, 2.5), (83000, 10),
    (48000, 1.9), (63000, 4.2)
]

salary_by_tenure = defaultdict(list)

for salary,tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

avarege_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print("\nSalário médio por tempo de experiência:")
for tenure, avg_salary in avarege_salary_by_tenure.items():
    print(f"{tenure} anos: ${avg_salary}")

def tenure_bucket(tenure):
    if tenure < 2:
        return "menos de dois anos"
    elif tenure < 5:
        return "entre dois e cinco anos"
    else:
        return "mais de cinco anos"
    
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

avarege_salary_by_bucket = {
    bucket: sum(salaries) / len(salaries)
    for bucket, salaries in salary_by_tenure_bucket.items()
}

print("\nSalário médio por faixa de tempo de experiência:")
for bucket, avg_salary in avarege_salary_by_bucket.items():
    print(f"{bucket}: ${avg_salary}")

# TÓPICOS DE INTERESSE

words_and_counts = Counter(word
    for user, interest in interests
    for word in interest.lower().split()
)

print("\nPalavras mais comuns nos interesses:")
for word, count in words_and_counts.most_common():
    if count > 1:
        print(f"{word}: {count}")

# FIM DO PRIMEIRO DIA
