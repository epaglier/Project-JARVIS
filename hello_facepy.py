from facepy import GraphAPI

access_token = "EAACEdEose0cBAHfk4USidrp2VZBdweRQkKLjYBXM3EayZBcGjiY2mzMJiY0LiawUmZAbHXvIiFQZAnuqvqcoZAJZBMHWpt7HzieyAOz5aFA15DLZB8eeuaDXdzCVQHYiREDQiaiLAq3EcjFHTfW3DjRf65uLNcGadXElaOVNCVhHNiNswSYB0uyJK1QzTq7jRShtZCndw0gyZAAZDZD"
graph = GraphAPI(access_token)

# Get my latest posts

p = []
p = graph.get('me/feed')
print p
