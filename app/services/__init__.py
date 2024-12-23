# from groq import Groq
#
# from app.utils.csv_utils import convert_groq_to_dict
#
#
# def groq_region_and_targt(row):
#     client = Groq(api_key="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",)
#     completion = client.chat.completions.create(
#         model="llama3-8b-8192",
#         messages=[
#             {
#                 "role": "user",
#                 "content": f"{row}.\"\n\n\nI need you to return me the region of the world it happened from among the following regions: ['Central America & Caribbean', 'North America', 'Southeast Asia', 'Western Europe', 'East Asia', 'South America', 'Eastern Europe', 'Sub-Saharan Africa', 'Middle East & North Africa', 'Australasia & Oceania', 'South Asia', 'Central Asia']\n and the type of people the attack was aimed at (such as Jews, gypsies, policemen, government officials, Christians) with the fields region_txt, targtype_txt\nDon't give me back anything but this dictionary"
#             }
#         ],
#         temperature=1,
#         max_tokens=1024,
#         top_p=1,
#         stream=True,
#         stop=None,
#     )
#     response_content = ""
#     for chunk in completion:
#         response_content += chunk.choices[0].delta.content or ""
#     return response_content
#
# #
# # response_content = groq_region_and_targt("24-Feb-68,Masada,Israel,Other,Explosives,0,0,\"ISRAEL.  Palestinian terrorists fired five mortar shells into the collective settlement at Masada, causing slight damage but no injuries.\"")
# # result = convert_groq_to_dict(response_content)
# # print(result)
#
