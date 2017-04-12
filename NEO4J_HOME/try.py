#!/usr/bin/python2
from py2neo import authenticate,Graph,Node,Relationship
authenticate("localhost:7474", "neo4j", "cs315")
graph = Graph("http://localhost:7474/db/data/")
Node1 = Node("Word",Name="baby")
Node2 = Node("Word",Name="love")
Node3 = Node("Word",Name="sex")
Song1 = Node("Track",Name="Paris")
Song2 = Node("Track",Name="Closer")
Song3 = Node("Track",Name="Shape Of You")
Song4 = Node("Track",Name="Baby")
Song5 = Node("Track",Name="Firework")
Song6 = Node("Track",Name="We Are Young")

# graph.run(CREATE (Node1:Word {Name:"baby"}))
# graph.run(CREATE (Node2:Word {Name:"love"}))
# graph.run(CREATE (Node3:Word {Name:"sex"}))
Rel1 = Relationship(Song1, "Key", Node1)
Rel2 = Relationship(Song2, "Key", Node1)
Rel3 = Relationship(Song4, "Key", Node2)
Rel4 = Relationship(Song5, "Key", Node1)
Rel5 = Relationship(Song6, "Key", Node3)
Rel6 = Relationship(Song3, "Key", Node2)
Rel7 = Relationship(Song4, "Key", Node1)
Rel8 = Relationship(Song3, "Key", Node2)
Rel9 = Relationship(Song2, "Key", Node1)
Rel10 = Relationship(Song1, "Key", Node3)
Rel11 = Relationship(Song2, "Key", Node2)
Rel12 = Relationship(Song3, "Key", Node1)
graph.create(Node1)
graph.create(Node2)
graph.create(Node3)
graph.create(Song1)
graph.create(Song2)
graph.create(Song3)
graph.create(Song4)
graph.create(Song5)
graph.create(Song6)
# graph.run(CREATE (Song1-[:Key]->Node1))
# graph.run(CREATE (Song2-[:Key]->Node1))
# graph.run(CREATE (Song4-[:Key]->Node2))
# graph.run(CREATE (Song5-[:Key]->Node1))
# graph.run(CREATE (Song6-[:Key]->Node3))
# graph.run(CREATE (Song3-[:Key]->Node2))
# graph.run(CREATE (Song4-[:Key]->Node1))
# graph.run(CREATE (Song3-[:Key]->Node2))
# graph.run(CREATE (Song2-[:Key]->Node1))
# graph.run(CREATE (Song1-[:Key]->Node3))
# graph.run(CREATE (Song2-[:Key]->Node2))
# graph.run(CREATE (Song3-[:Key]->Node1))
graph.create(Rel1)
graph.create(Rel2)
graph.create(Rel3)
graph.create(Rel4)
graph.create(Rel5)
graph.create(Rel6)
graph.create(Rel7)
graph.create(Rel8)
graph.create(Rel9)
graph.create(Rel10)
graph.create(Rel11)
graph.create(Rel12)

results = graph.find("Word","Name","baby")
for result in results:
    print(result)
# 
# MATCH (pee1)-[:Key]->(n:Word {Name:"baby"})<-[:Key]-(pee2) WHERE pee1<>pee2 RETURN pee1,pee2,n
# FOREACH(p1 in pee1 |
#     FOREACH (p2 in pee2 |
#                 MATCH (p1)-[:Key]->(n:Word)<-[:Key]-(p2) WHERE p1<>p2)) RETURN p1,p2,n
#
# FOREACH(country in cou |
#     FOREACH (c in ch |
#             FOREACH (a in addresses |
#                 CREATE (s:Store {name:c.name+"_"+a, address:a})
#                 CREATE (s-[:BELONGS_TO]->c)
#                 CREATE (s-[:IN]->country)               )))


# for rel in graph.match(start_node=Node2, rel_type="Key"):
#     print(rel.end_node()["Name"])

# MATCH (n:Word {Name:"baby"})<-[:Key]-(pee)
# FOREACH (n IN nodes(pee))

# MATCH (n:Word {Name:"baby"})<-[:Key]-(pee) RETURN pee,n

