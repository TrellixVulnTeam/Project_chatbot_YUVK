from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
set_pairs = [#vandana
['Hi,Hello','Hello, this is AgroXpert chatbot.What is your query?'],
['quit,bye','I am always there at your service'],
["How many varieties of rice are grown in India?","Approximately 6,000 different varieties,But we have also lost tens thounsands of varieties from last 40 years"],
["which is the most popular rice grown in India?",'Basumati rice'],
["what is the history behind basumati rice ?","In 1997 American got patent over basumati rice by biopiracy"],
['what is  biopiracy?','Biopiracy is the commercial exploitation of naturally occurring biochemical or genetic material, without proper authorisation is known as biopiracy'],
['How many varieties of basumati are documented?','27 types of basumati rice are documented'],
['what is the life span of paddy,rice plant?','3-7 months'],
['In which month paddy is harvested?','In November-December the paddy should be harvested'],
['In which month paddy should be grown','we should start cultivating paddy in the month of june-july'],  
['How long does it take to harvest paddy?','It normally takes 3 months to harvest paddy'],
['how is rice stored after harvesting?',' it should be threshed immediately after harvesting and maintain it by storing the grains at ambient temperature and Humidity <60% in dedicated area'],
['How to protect the rice from pest?','Using pesticides or by packing the well treated, quality rice'] ,
['what should we do after harvesting?','After harvesting it should be dried to certain duration,in certain temperature and store it.Delays in drying, incomplete drying or ineffective drying will reduce grain quality and result in losses'],
['why are paddy fields drained?','Mid-season drainage reduces methane emissions of paddy fields, with reductions ranging from 7 to 95%'],
['when is paddy fields drained?','About 7 days towards the end of tillering in the middle of the season'],
['what are the steps taken to grow paddy?','preparation of fields,transplantations or seedling,field maintenance,threshing,winnowing and milling'],
['How field is prepared for growing paddy?','Removal of weeds,ploughing the field,adding mannures and fertilizers,covered with water of about 2.5 cm,seedling'],
['How seedling is done?','Sown directly in the field and the seedlings sprout when the rain comes'],
['How is seedling  done?','Sown directly in the field and the seedlings sprout when the rain comes'],
['how is transplating of seed is done?','Manual transplanting is done either at random or in straight-rows'],
['what is random transplanting method?','seedlings are transplanted without a definite distance or space between plants'],
['what is straight-row transplanting?','The straight-row method follows a uniform spacing between plants'],
['who are you?','I am a chatbot, My name is AgroXpert'],
['which type of soil is used for growing rice,paddy?,what kind of land is needede for growing rice,paddy?','Rice grows on a variety of soils like silts, loams and gravels in India'],
['what can you do?,what do you know?','I am AgroXpert, I can help you by answering your queries regarding farming'],
['At what temperature rice is grown?','approx. 25 degree Celsius'],
['Which State is the Biggest Rice Producer in India?,which is the largest rice producing state in India?','West bengal'],
['How can we increase rice prouction?,how to increase the production of rice?','The three factors that could contribute to increased rice productivity are: (a) developing new rice varieties including hybrids with higher yield potential; (b) minimizing the yield gap between what is currently harvested by farmers and the achievable highest on-farm yield of varieties they grow; and (c) reducing the post-harvest losses and improving grain quality to enhance profitability'],
['which fertilizer,fertilizers is,are used for rice?','Fertilizer containing Nitrogen (N), phosphorus (P), and potassium (K) is best for rice '],
]
print("Hi, I'm the AgroXpert,Have doubts on farming?I am here to help you\n") 
#creating a new chatbot
chatbots = ChatBot(name='AgroXpert', read_only=True,
                 logic_adapters=[
                     {
                         'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I do not understand. I am still learning. Please contact abc@xxx.com for further assistance.',
                     'maximum_similarity_threshold': 0.7

                         }])
trainer = ListTrainer(chatbots)
for item in set_pairs:
    trainer.train(item)
# Create your views here.
from django.shortcuts import render

# Create your views here.
def Chatbots(request):
    Reply=""
    query=""
    if request.method=="POST":
        query=request.POST["Search"]
        Reply=chatbots.get_response(query)
    return(render(request,'chatbot.html',{"Reply":Reply,"query":query}))
