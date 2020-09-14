from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

today = datetime.today()


class ToDoList:

    def choice(self):
        choice = int(input("""
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
"""))
        if choice == 1:
            self.one()
        elif choice == 2:
            self.two()
        elif choice == 3:
            self.three()
        elif choice == 4:
            self.four()
        elif choice == 5:
            self.five()
        elif choice == 6:
            self.six()
        elif choice == 0:
            print("\nBye!")
            exit()

    @staticmethod
    def one():
        print(f"\nToday {today.day} {today.strftime('%b')}:")
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for i in range(len(rows)):
                print(f'{i + 1}. {rows[i]}')

    @staticmethod
    def two():
        for i in range(7):
            ffdays = today + timedelta(days=i)
            rows = session.query(Table).filter(Table.deadline == ffdays.date()).all()
            print(f'\n{ffdays.strftime("%A")} {ffdays.day} {ffdays.strftime("%b")}:')
            if len(rows) == 0:
                print('Nothing to do!')
            else:
                for j in range(len(rows)):
                    print(f'{j + 1}. {rows[j]}')

    @staticmethod
    def three():
        print("\nAll tasks:")
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print('Nothing to do!')
        else:
            for i in range(len(rows)):
                print(f'{i + 1}. {rows[i]}. {rows[i].deadline.strftime("%d")} {rows[i].deadline.strftime("%b")}')

    @staticmethod
    def four():
        print("\nMissed tasks:")
        rows = session.query(Table).filter(Table.deadline < today.date()).order_by(Table.deadline).all()
        if len(rows) == 0:
            print('Nothing is missed!')
        else:
            for i in range(len(rows)):
                print(f'{i + 1}. {rows[i]}. {rows[i].deadline.strftime("%d")} {rows[i].deadline.strftime("%b")}')

    @staticmethod
    def five():
        task_ = input("\nEnter task\n")
        deadline_ = input("Enter deadline\n")
        new_row = Table(task=task_, deadline=datetime.strptime(deadline_, '%Y-%m-%d'))
        session.add(new_row)
        session.commit()
        print('The task has been added!')

    @staticmethod
    def six():
        rows = session.query(Table).order_by(Table.deadline).all()
        if not rows:
            print('Nothing to delete')
        else:
            print("\nChoose the number of the task you want to delete:")
            for i in range(len(rows)):
                print(f'{i + 1}. {rows[i]}. {rows[i].deadline.strftime("%d")} {rows[i].deadline.strftime("%b")}')
            session.delete(rows[int(input()) - 1])
            session.commit()
            print('The task has been deleted!')


while True:
    tdl = ToDoList()
    tdl.choice()
