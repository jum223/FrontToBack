import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from PIL import Image

# Load data
data = pd.read_csv("OutputData/final.csv")
data["Date"] = pd.to_datetime(data['Date'])
event_date = pd.read_csv("InputData/MajorEvents.csv")
event_date['Date'] = pd.to_datetime(event_date['Date']) # convert Date column to datetime format
ret_diffs = pd.read_csv("OutputData/RetDiff.csv")
ret_diffs["Date"] = pd.to_datetime(ret_diffs['Date'])
img = Image.open('pics/Garganta.png')

print("is this coming through")
"""
# Industry Returns throughout the Russia-Ukraine War
#### Industry Returns around major events in the armed conflict
"""

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Analysis"])

    if page == "Home":
        
        ## Added code inside
        # Create a sidebar with a dropdown menu
        # Create a sidebar with a dropdown menu
        options1 = ['Metal', 'Energy', 'Semiconductor', "Transport", "Food"]
        all_option1 = 'All of Them'
        if st.sidebar.checkbox('Select all industries', False):
            option1 = [all_option1]
        else:
            option1 = st.sidebar.multiselect('Which industries do you want to visualize?', options1)

        # Highlight event date
        option2 = st.sidebar.selectbox(
            'Which event do you want to visualize?',
             event_date['Event'].unique())
        
        st.sidebar.markdown("[To see the code which produces the visualizations please visit the project repo](https://github.com/jum223/FrontToBack)")

        # Filter data based on selected options
        if all_option1 in option1:
            data_filtered = data.copy()
        else:
            data_filtered = data.query("Industry in @option1")
            
        sns.set_style("whitegrid", {'axes.grid': True, 'grid.color': '.8', 'grid.linestyle': '-'})

        # Create plot
        if option1 or (all_option1 in option1):
            fig, ax = plt.subplots()
            if all_option1 in option1:
                for ind in data_filtered["Industry"].unique():
                    industry_df = data_filtered[data_filtered['Industry'] == ind]
                    sns.lineplot(x='Date', y='Cum_ret', data=industry_df, label=ind, ax=ax, ci=None)
            else:
                for col in option1:
                    industry_df = data_filtered[data_filtered['Industry'] == col]
                    sns.lineplot(x='Date', y='Cum_ret', data=industry_df, label=col, ax=ax, ci=None)


            date = event_date.loc[event_date['Event'] == option2, 'Date'].iloc[0]

            plt.axvline(date, color='red', linestyle='--', label='Event Date')

            plt.xlim(date - pd.Timedelta(days=20), date + pd.Timedelta(days=20))

            # set x-axis ticks
            xticks = [date - pd.Timedelta(days=20), date, date + pd.Timedelta(days = 3),date + pd.Timedelta(days = 10), date + pd.Timedelta(days=20)]
            xticklabels = ['t-20', date.strftime('%Y-%m-%d'), "t+3", "t+10", 't+20']
            plt.xticks(xticks, xticklabels)
            plt.xticks(rotation=45)
            sns.despine(right=True, top=True, bottom = True, left = True)

            # add title and axis labels
            plt.title('Cumulative Returns by Industry')
            plt.xlabel('Date')
            plt.ylabel('Cumulative Return')

            # move the legend to the bottom right corner
            plt.legend(loc='upper left')

            ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
            #ax.set_axis_off()


            # show the plot
            st.pyplot(fig)

        else:
            st.image(img, caption='Ukrainian Soldiers')

        if all_option1 in option1:
            industries = ret_diffs['Industry'].unique()
        else:
            industries = option1

        # Divide the page into equal-sized columns
        col1, col2, col3 = st.columns(3)

        if option1:
            if all_option1 in option1:
                for i, industry in enumerate(industries):
                    industry_returns_filtered = ret_diffs[(ret_diffs['Industry'] == industry) & (ret_diffs['Date'] == date)]
                    box_content = []
                    for _, row in industry_returns_filtered.iterrows():
                        ret3_value = row['ret3'] * 100
                        ret3_color = 'red' if ret3_value < 0 else 'green'
                        ret3_str = f"{ret3_value:.2f}%"
                        ret3_display = f"% difference t+3: <span style='color:{ret3_color};'>{ret3_str}</span>"
                        box_content.append(ret3_display)
                        ret10_value = row['ret10'] * 100
                        ret10_color = 'red' if ret10_value < 0 else 'green'
                        ret10_str = f"{ret10_value:.2f}%"
                        ret10_display = f"% difference t+10: <span style='color:{ret10_color};'>{ret10_str}</span>"
                        box_content.append(ret10_display)
                    # Display the box in the appropriate column
                    if i % 3 == 0:
                        box_column = col1
                    elif i % 3 == 1:
                        box_column = col2
                    else:
                        box_column = col3
                    with box_column:
                        st.subheader(industry + ' Returns')
                        st.markdown("<br>".join(box_content), unsafe_allow_html=True)

            else:
                for i, industry in enumerate(industries):
                    industry_returns_filtered = ret_diffs[(ret_diffs['Industry'] == industry) & (ret_diffs['Date'] == date)]
                    box_content = []
                    for _, row in industry_returns_filtered.iterrows():
                        ret3_value = row['ret3'] * 100
                        ret3_color = 'red' if ret3_value < 0 else 'green'
                        ret3_str = f"{ret3_value:.2f}%"
                        ret3_display = f"% difference t+3: <span style='color:{ret3_color};'>{ret3_str}</span>"
                        box_content.append(ret3_display)
                        ret10_value = row['ret10'] * 100
                        ret10_color = 'red' if ret10_value < 0 else 'green'
                        ret10_str = f"{ret10_value:.2f}%"
                        ret10_display = f"% difference t+10: <span style='color:{ret10_color};'>{ret10_str}</span>"
                        box_content.append(ret10_display)

                    if i % 3 == 0:
                        box_column = col1
                    elif i % 3 == 1:
                        box_column = col2
                    else:
                        box_column = col3
                    with box_column:
                        st.subheader(industry + ' Returns')
                        st.markdown("<br>".join(box_content), unsafe_allow_html=True)
                        
                # Adding Event Descriptions
        if option1 or (all_option1 in option1):
            if option2 == "Invasion Announcement":
                """
                ## Invasion Announcement:
                ##### Febuary 24, 2022
                """
                "In the early hours of February 24, Russian President Vladimir Putin ordered his troops into Ukraine. Kyiv’s Western allies had been warning of looming Russian aggression for months. Still, Putin’s decision came as a shock to many in Ukraine and across the world. Speaking on Russian state television, he announced the launch of what he called a “special military operation” to “demilitarize” and “denazifiy” Ukraine. Moments later, the first explosions were heard across Ukraine."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "Following Russia's invasion of Ukraine, metals and energy sectors experienced positive returns of 6.06% and 7.00% respectively, after 3 days, due to increased commodity prices and supply concern. Meanwhile, transport, food, and semiconductors sectors faced negative returns of -0.06%, -1.62%, and -3.8% respectively after 3 days, as a result of potential supply chain disruptions and broader market uncertainty. The conflict's impact on these sectors reflects its far-reaching consequences on global markets and industries."
            elif option2 == "Ukraine announces it will defend its territory":
                """
                ## Ukraine announces it will defend its territory: 
                ##### Febuary 25, 2022
                """
                "Amid the chaos of the opening hours of the war, rumors started to swirl about Ukraine’s leadership fleeing the country. Ukrainian President Volodymyr Zelensky and his team reacted by filming a video of themselves in central Kyiv, reassuring the nation. “We are all here defending our independence, our state and it will remain so. Glory to our defenders! Glory to our women defenders! Glory to Ukraine!” Zelensky said. The president had refused a US offer to evacuate, according to the Ukrainian government, saying: “I need ammunition, not a ride.“"
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "One day after Russia announces their invasion, Ukraine announces that they will defend their territory and fight for their country. As this news comes only one day after the invasion announcement, industry returns for the metal, energy, transporation, food, and semiconductor does not change drastically enough to make a new supportive analysis statement."
            elif option2 == "Refugee Crisis in Poland": 
                """
                ## Refugee Crisis in Poland:
                ##### March 2, 2022
                """
                "The brutality of Russia’s invasion forced hundreds of thousands of Ukrainian civilians to flee the country. The United Nations’ refugee agency (UNHCR) said that at least 100,000 people had left their homes in the first 24 hours of the military assault. Thousands of cars formed queues at the borders, with people waiting several days to cross into neighboring Poland. Many others fled by train, waiting at train stations for days to cram into overcrowded carriages. The majority were women, children and the elderly, as men of fighting age were largely prohibited from leaving the country."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "As the refugee crisis in Poland grows as hundreds of thousands are forced from their homes, the following occured to each of the industry sectors. The metal sector experienced 3.81% growth at t+3, likely driven by increased demand and regional uncertainty. Transport returns initially declined by 4.64% at t+3 due to disrupted logistics and increased fuel costs. The energy sector saw an 11.34% increase at t+3, attributed to potential supply disruptions and heightened demand. Food returns grew by 2.12% at t+3, driven by the increased demand to meet the needs of the refugee population. Lastly, the Microchip sector returns declined by 5.63% at t+3, possibly due to supply chain disruptions and broader market uncertainty."
            elif option2 == "Irpin Bridge Evacuation":
                """
                ## Irpin Bridge Evacuation
                ##### March 6, 2022
                """
                "As Russian troops began to approach Kyiv, people living in the northwestern suburbs of the capital got caught up in some of the heaviest street-by-street fighting of the war so far. The main bridge crossing the Irpin River was destroyed by Ukrainians to thwart a Russian advance, which made evacuations difficult. According to the Ukrainian authorities, hundreds of civilians died attempting to flee."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "Following the Irpin Bridge Evacuation, metal returns saw a moderate growth of 2.45% at t+3, possibly influenced by regional uncertainty and increased demand for resources."
            elif option2 == "Mariupol Hospital Attack":
                """
                ## Mariupol Hospital Attack
                ##### March 9, 2022
                """
                "A maternity hospital in the southeastern city of Mariupol was hit by a Russian missile. The attack came despite Russia agreeing to a 12-hour pause in hostilities to allow refugees to evacuate. A photo of a pregnant woman injured in the bombing being carried on a stretcher outside the devastated hospital became emblematic of Russia’s senseless aggression against its neighbor."
            elif option2 == "Mariupol Theater Bombing":
                """
                ## Mariupol Theater Bombing
                ##### March 16, 2022
                """
                "The bombing of Mariupol’s Drama Theater was among the most brazen of Russia’s attacks on civilians. Ukrainian officials estimated 1,300 people were sheltering in the theater in the centre of a city which had, at that point, been under siege for weeks. Around 300 died that day, authorities said at the time, but subsequent reports suggested the death toll could be higher. Russia, which had been bombarding the city for weeks, denied its forces were responsible."
            elif option2 == "War crimes uncovered":
                """
                ## War crimes uncovered
                ##### April 1, 2022
                """
                "When Russian troops withdrew from Bucha in early April, they left behind a trail of destruction — and evidence of summary executions, brutality and indiscriminate shelling. Images showing dozens of bodies of civilians scattered around a single street in Bucha prompted calls for Russia to be investigated for war crimes. Russia made baseless claims that the images were fake and has prosecuted several Russian journalists and dissidents who spoke up about the killings for spreading “false information” about the war. International experts from the Organization for Security and Cooperation in Europe said they found “grave breaches” of international humanitarian law by Russian forces."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "The percentage change in returns 3 days after the war crimes were uncovered resulted in negative returns for most industries except the semiconductor industry, which had returns increase by 0.67%, while the rest ranged from -0.57% to -1.32%. The longer term returns, 10 days after the event showed a split between industries. The food, energy and metal industries all had positive returns, 4.65%, 1.22% and 1.22% respectively. The transport and semiconductor industries had major decreases in returns, -4.83% and -9.38% respectively."
            elif option2 == "Sunking of Russian main ship":
                """
                ## Sunking of Russian main ship
                ##### April 14, 2022
                """
                "Moskva, the flagship of Russia’s Black Sea fleet, sank on April 14. The cause remains disputed. Ukraine said it hit the Moskva with anti-ship cruise missiles, sparking a fire that detonated stored ammunition. Russia blamed a fire of unknown origin. Whatever the reason, the loss of the guided-missile cruiser was a major military embarrassment for Russia and its biggest wartime loss of a naval ship in 40 years."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "3 days after the sinking of the Russian flagship, most industries were on level with their reaction to this event, returns ranged between -0.66% and 1.25%, worst and best of being the food and energy industries respectively. 10 days after the event returns ranged from -7.03% and 4.31%, both extremes being that of the energy and transport industries."
            elif option2 == "Mariupol Steel Plant Defence":
                """
                ## Mariupol Steel Plant Defence
                ##### May 17, 2022
                """
                "The sprawling Azovstal steel plant in Mariupol became another symbol of Ukrainian resistance in the face of a much larger enemy. Defenders of the plant withstood weeks of relentless Russian bombardment before finally surrendering in May. Ukrainian officials praised the fighters, saying their fierce defense of the complex had stalled Russian forces and prevented the capture of Zaporizhzhia, further west."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "3 days after the successful defense by Ukrainian troops at the Mariupol Steel Plant, stock returns varied from -1.79% through 1.71%, the transportation having the lowest and the energy industry with the highest returns. 10 days after the event, returns varied significantly between industries. The food industry had the lowest returns with a -3.11% and the energy industry had the highest returns, with 7.27%."
            elif option2 == "Russian retreat from Kharkiv":
                """
                ## Russian retreat from Kharkiv
                ##### September 1, 2022
                """
                "A blistering Ukrainian counteroffensive in eastern Ukraine in September recaptured large swaths of territory and forced Russian troops to flee the Kharkiv region. Moscow tried to spin the hasty withdrawal as “regrouping.” But in a sign of just how badly things were going for Russia, the military was publicly criticized by a number of high-profile Kremlin loyalists including Chechen leader Ramzan Kadyrov, who supplied thousands of fighters to the offensive."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "3 days after the Russian retreat from Kharkiv, returns varied slightly for most firms. The food industry had returns -0.41%, thus being the lowest and the highest was the energy industry with 3.84%. 10 days after the event, the food industry had the lowest returns with -3.40%, and the highest was the metal industry, with 2.58%."
            elif option2 == "Russia starts mobilization":
                """
                ## Russia starts mobilization
                ##### September 21, 2022
                """
                "Following a string of embarrassing defeats in Ukraine, Putin announced Russia’s first mobilization since World War II on September 21. The controversial draft sparked protests — a rare sight in Russia — and an exodus of men of fighting age from the country. The partial mobilization was beset by errors and produced fighters that were poorly equipped and largely untrained. However, it significantly increased Russia’s troop numbers."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "3 days after Russia started its mobilization effort, all the industries acted differently to this event. The energy industry had the lowest returns, of -7.10%, while the food industry had the highest returns with 0.87%. 10 days after the event, returns were split between all industries. The industries with positive returns were the food and energy industries, 0.84% and 1.10% respectively. The metal, transportation, and semiconductor industries all had decreasing returns, -0.11%, -1.03%, and -1.26% respectively."
            elif option2 == "Crimea Bridge Attack":
                """
                ## Crimea Bridge Attack
                ##### October 8, 2022
                """
                "In another major blow to Moscow, the only bridge connecting Russia with the Crimean Peninsula was severely damaged by an explosion. The Kerch Strait road-and-rail bridge is both strategically important and hugely symbolic. It was opened by Putin in 2018, four years after Russia illegally annexed Crimea from Ukraine."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "Most industries’ return differences from the date of the event to the given time frames seem to oscillate around a certain range of percentage differences, suggesting that this event didn’t have much significance on the operations or supply chains of the businesses in these industries. Nevertheless, the semiconductor industry did observe a decrease in returns, 3 days after such an event returns decreased by 3.08%, and 10 days after the event industry returns decreased even further to 6.6% approximately. The reason for this could be that the attack on the bridge supposed a greater threat to the supply of food products than any other industry."
            elif option2 == "Kyiv Blackout":
                """
                ## Kyiv Blackout
                ##### October 10, 2022
                """
                "A new phase of the war began when Russia launched the first of several waves of missile strikes on Ukraine’s critical energy infrastructure. Using missiles, artillery shells and Iranian-made drones, Moscow began targeting Ukrainian power facilities, leaving large areas of the country without power and water."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "From this visualization, it is notable to see how the energy industry saw a steady increase in returns post Kyiv blackout. This event involved several waves of missile strikes on Ukraine’s critical energy infrastructure, so it is not surprising to see this trend. After the event, Ukraine probably demanded a greater supply of energy in the form of oil or natural gas from its allied counterparts leading to increased returns in the energy industry as a consequence"
            elif option2 == "Kherson city liberation":
                """
                ## Kherson city liberation
                ##### November 12, 2022
                """
                "After eight months of brutal Russian occupation, the southern city of Kherson was liberated on November 12, prompting scenes of celebration by residents. Russia’s hasty withdrawal from the west bank of the Dnipro River was another bleak moment for Moscow, since Kherson was the only Ukrainian regional capital that Russian forces had captured. Putin himself had formally declared Kherson to be Russian territory just weeks before his troops’ retreat."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "Judging by the visualization produced, it seems like the Kherson city liberation did not have much of an effect on the returns of the different industries, we don’t see an abrupt change in returns in none of the industries shortly after the event. Nevertheless, it is apparent that the semiconductor industry started observing decreased returns starting 10 days after the event. Given the longer time frame other factors outside of the war could be causing the materialization of this phenomenon, but it could also be argued that this could be due to increased disruptions in the supply chain."
            elif option2 == "Zelensky visits White House":
                """
                ## Zelensky visits White House
                ##### December 21, 2022
                """
                "On December 21, Zelensky traveled to Washington, DC to meet with US President Joe Biden at the White House and to address the US Congress. It was a historic and consequential visit, the first foreign trip Zelensky had made since Russia launched its invasion. Just ahead of Zelensky’s arrival, the Biden administration announced it was sending nearly $2 billion in additional security assistance to Ukraine — including a sophisticated new Patriot air defense system."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "The strengthening of relationships between the Western world represented by the United States and Ukraine doesn’t seem to have much of an effect on industry returns shortly after the event. However, between 10 days and 20 days after the attack, all industry returns appear to increase except the food industry which continues on a downward trend since the event date."
            elif option2 == "Germany sends tanks":
                """
                ## Germany sends tanks
                ##### January 25, 2023
                """
                "After weeks of geopolitical squabbling, a major moment arrived on January 25 when Germany announced it would provide Leopard 2 tanks to Kyiv and allow other European countries to export the German-made battle tank. At the same time, Biden said the US would send 31 M1 Abrams tanks to Ukraine. The move was hailed as a breakthrough in the West’s military support for Ukraine and signaled a bullish view in the West about Ukraine’s ability to reclaim occupied territory."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "The line graph shows how industries are for the most part unaffected by such a crucial event that marked a turning point in the West’s military aid policy during the war. The only significant trend observed for all industries is the abrupt decrease in returns observed between 3 days and 10 days after the event, which in this case is due to an announcement of an increase in interest rates by the Fed on February 1st."
            elif option2 == "Biden visits Kyiv":
                """
                ## Biden visits Kyiv
                ##### February 20, 2023
                """
                "Biden made a highly symbolic surprise visit to Kyiv on February 20, his first since Russia’s full-scale invasion. Standing alongside Zelensky, the US president recalled how the pair spoke by phone as Russian forces rolled in. “One year later, Kyiv stands. And Ukraine stands. Democracy stands,” Biden declared. “The Americans stand with you and the world stands with you.” Zelensky said Biden’s visit brought Ukraine “closer to victory.” The two leaders went on a walkabout in Kyiv just as air raid sirens sounded across the city."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "As seen in the graph, the only industry which saw a decrease in returns shortly after the event is the metals industry with a decrease of 0.82%. The rest of the industries increased their returns anywhere in the range of 1% to 1.75% approximately. In the longer time frame 10 days after the event, all industries continued with this upward trend in returns, with the metal industry seeing the greatest increase in terms of percentage magnitude with 6.92%."


    elif page == "Analysis":
        st.title("Analysis")
        st.write("Add your analysis here.")

if __name__ == "__main__":
    main()


