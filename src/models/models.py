from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base, uniq_str_an
import enum
from sqlalchemy import text

class User(Base):
    username: Mapped[uniq_str_an]
    email: Mapped[uniq_str_an]
    password: Mapped[str]
    # profile_id: Mapped[int | None] = mapped_column(ForeignKey('profiles.id'))

# class GenderEnum(str, enum.Enum):
#     MALE = "мужчина"
#     FEMALE = "женщина"

# class ProfessionEnum(str, enum.Enum):
#     DEVELOPER = "разработчик"
#     DESIGNER = "дизайнер"
#     MANAGER = "менеджер"
#     TEACHER = "учитель"
#     DOCTOR = "врач"
#     ENGINEER = "инженер"
#     MARKETER = "маркетолог"
#     WRITER = "писатель"
#     ARTIST = "художник"
#     LAWYER = "юрист"
#     SCIENTIST = "ученый"
#     NURSE = "медсестра"
#     UNEMPLOYED = "безработный"
    
# class Profile(Base):
#     first_name: Mapped[str]
#     last_name: Mapped[str | None]
#     age: Mapped[int | None]
#     gender: Mapped[GenderEnum]
#     profession: Mapped[ProfessionEnum] = mapped_column(
#         default=ProfessionEnum.DEVELOPER,
#         server_default=text("'UNEMPLOYED'")
#     )
#     interests: Mapped[List[str] | None] = mapped_column(ARRAY(String))
#     contacts: Mapped[dict | None] = mapped_column(JSON)

# class StatusPost(str, enum.Enum):
#     PUBLISHED = "опубликован"
#     DELETED = "удален"
#     UNDER_MODERATION = "на модерации"
#     DRAFT = "черновик"
#     SCHEDULED = "отложенная публикация"

# class Post(Base):
#     title: Mapped[str]
#     content: Mapped[Text]
#     main_photo_url: Mapped[str]
#     photos_url: Mapped[List[str] | None] = mapped_column(ARRAY(String))
#     status: Mapped[StatusPost] = mapped_column(default=StatusPost.PUBLISHED, server_default=text("'DRAFT'"))
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))    