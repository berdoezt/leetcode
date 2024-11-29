from enum import Enum
import uuid

class VoteType(Enum):
    VOTE_UP = 1
    VOTE_DOWN = 2

class Post:
    def __init__(self, content, author) -> None:
        self.__id: str = str(uuid.uuid4())
        self.__content: str = content
        self.__comment : list[Comment] = []
        self.__author : User = author
        self.__vote : int = 0
    
    def vote(self, type: VoteType):
        if type == VoteType.VOTE_UP:
            self.__vote += 1
        elif type == VoteType.VOTE_DOWN:
            self.__vote -= 1
        
        return self.__vote
    
    def add_comment(self, comment):
        self.__comment.append(comment)
        return comment
    
    def get_content(self):
        return self.__content

    def get_author(self):
        return self.__author
    
    def get_vote(self):
        return self.__vote
    
class Answer(Post):
    def __init__(self, content, author) -> None:
        super().__init__(content, author)

class Question(Post):
    def __init__(self, title, content, author, tags) -> None:
        super().__init__(content, author)
        self.__title: str = title
        self.__tags : list[str] = tags
        self.__answers : list[Answer] = []
    
    def add_answer(self, answer: Answer):
        self.__answers.append(answer)
        return answer
    
    def add_tag(self, tag):
        self.__tags.append(tag)
        return tag

    def get_answers(self):
        return self.__answers
    
    def get_title(self):
        return self.__title
    
    def get_tags(self):
        return self.__tags
    pass

class User:
    def __init__(self, username) -> None:
        self.__id: str = str(uuid.uuid4())
        self.__username: str = username
        self.__questions : list[Question] = []
        self.__answer : list[Answer] = []
        self.__comment : list[Comment] = []
    pass

    def ask_question(self, title, content, tags):
        question = Question(title, content, self, tags)
        self.__questions.append(question)
        return question
    
    def get_questions(self):
        return self.__questions
    
    def answer_question(self, question: Question, content):
        answer = Answer(content, self)
        question.add_answer(answer)
        self.__answer.append(answer)
        return answer
    
    def add_comment(self, post: Post, content):
        comment = Comment(content, self)
        post.add_comment(comment)
    
class Comment:
    def __init__(self, content, author) -> None:
        self.__id: str = str(uuid.uuid4())
        self.__content: str = content
        self.__author: User = author
    
    def get_content(self):
        return self.__content
    pass

if __name__ == "__main__":
    dylan = User("dylan")
    satya = User("satya")

    question = dylan.ask_question("judul", "cara cepet kaya ?", ["dukun", "pelet"])
    satya.answer_question(question, "kerja mas'e")
    question.add_tag("kaya")
    question.vote(VoteType.VOTE_UP)

    questions = dylan.get_questions()
    for question in questions:
        print(question.get_content(), question.get_title(), question.get_vote(), question.get_tags())
        for answer in question.get_answers():
            print(answer.get_content())
