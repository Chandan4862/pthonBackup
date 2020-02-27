climate="Climate change occurs when changes in Earth's climate system result in new weather patterns that remain in place for an extended period of time. This length of time can be as short as a few decades to as long as millions of years. The climate system receives nearly all of its energy from the sun, with a relatively tiny amount from earth's interior. The climate system also gives off energy to outer space. The balance of incoming and outgoing energy, and the passage of the energy through the climate system, determines Earth's energy budget. When the incoming energy is greater than the outgoing energy, earth's energy budget is positive and the climate system is warming. If more energy goes out, the energy budget is negative and earth experiences cooling."
gst="Goods and Services Tax (GST) is an indirect tax (or consumption tax) imposed in India on the supply of goods and services. It is a comprehensive multistage, destination based tax: comprehensive because it has subsumed almost all the indirect taxes except few; multi-staged as it is imposed at every step in the production process, but is meant to be refunded to all parties in the various stages of production other than the final consumer and as a destination based tax, as it is collected from point of consumption and not point of origin like previous taxes."
ai="Artificial Intelligence (AI) is transforming the nature of almost everything which is connected to human life e.g. employment, economy, communication, warfare, privacy, security, ethics, healthcare etc. However, we are yet to see its evolution in long-term, whether it's leading humanity towards making this planet a better place to live or a place which is full of disaster. Every technology has its advantages and disadvantages but advantages always outweigh disadvantages for the technology to survive in the market. Nonetheless, for Artificial Intelligence we are not yet sure whether in the long-term positive effects will always keep outweighing the negative effects and if that is not the case then we are in serious trouble. If we look around us, on the one hand, we seem to embrace the change being brought by technology, be it smart home, smart healthcare, Industry 4.0 or autonomous cars. On the other hand, we often found ourselves protesting against the government in the context of unemployment, taxes, privacy etc. As AI development is speeding up, more robots or autonomous systems are being born and replacing the human labor. This is the current situation; however, in long-term, results seem to get more interesting. Throughout this essay, I will cover the major domains where human life is significantly affected by AI in both positive and negative ways."
str="my name is chandam"

climate=climate.split(" ")
gst=gst.split(" ")
ai=ai.split(" ")

setClimate={""}
setGst={""}
setAi={""}

for i in climate:
    setClimate.add(i)
for i in gst:
    setGst.add(i)
for i in ai:
    setAi.add(i)

#  Only common words from A and C

print("common Words from Climate and Ai \n",setClimate.intersection(setAi),"\n")

#  True or false : len( A U C ) < len( B )

print("len( A U C ) < len( B ):::",len(setClimate.union(setAi))< len(setGst),"\n")

# All the words of B but not in A as well as not in C

print(" All the words of B but not in A as well as not in C\n\n",setGst.difference(setClimate).difference(setAi))