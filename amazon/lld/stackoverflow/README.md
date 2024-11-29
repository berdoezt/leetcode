Requirements:
1. User can post questions, answer questions, comment on answer and question
2. User can vote on the question and answer
3. Question can have tags
4. User can search questions based on the tag or the title

Core Entity:
1. User : represent the person who interact with the system
2. Question : represent the question asked by user
3. Answer : represent the answer of a question that created by user
4. Tag : represent a tag on a question
5. Comment : represent comment on the answer / comments created by user
6. Vote : represent vote on the answer / question created by user

Entity Relationship
1. User can ask many Question, provide many Answers, give many Comment
2. Question have many Answer, many Comment, many Vote, and many Tag
3. Answer, Comment, Vote, and Tag can't be exist alone
4. Answer have many Comment and Vote