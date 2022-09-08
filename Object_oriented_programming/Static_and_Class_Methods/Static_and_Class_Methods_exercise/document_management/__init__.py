from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.document_management.category import Category
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.document_management.document import Document
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.document_management.storage import Storage
from Object_oriented_programming.Static_and_Class_Methods.Static_and_Class_Methods_exercise.document_management.topic import Topic
c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize document_management")
d1.add_tag("urgent")
d1.add_tag("work")
storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)
print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
