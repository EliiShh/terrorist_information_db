# from sqlalchemy import create_engine, text
# from sqlalchemy.exc import OperationalError
#
#
#
# def check_connection():
#     try:
#         # יצירת engine עם ה-psql_url
#         engine = create_engine("postgresql+psycopg2://admin:1234@172.27.121.182:5432/attacks")
#
#         # ניסיון להתחבר
#         with engine.connect() as connection:
#             # שליחה של שאילתת בדיקה פשוטה כדי לוודא שהחיבור תקין
#             connection.execute(text("SELECT * from cities;"))
#             print("החיבור למסד הנתונים הצליח!")
#             return True
#     except OperationalError as e:
#         # אם החיבור נכשל
#         print(f"נכשל בהתחברות למסד הנתונים: {e}")
#         return False
#
#
# check_connection()