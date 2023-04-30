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
img = Image.open('pics/WarImage.png')

"""
# Industry Returns throughout the Russia-Ukraine War
#
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

        # Filter data based on selected options
        if all_option1 in option1:
            data_filtered = data.copy()
        else:
            data_filtered = data.loc[:, ['Date'] + option1]

        # Create plot
        if option1 or (all_option1 in option1):
            sns.set_style('darkgrid')
            fig, ax = plt.subplots()
            if all_option1 in option1:
                for col in data_filtered.columns[2:]:
                    sns.lineplot(x='Date', y=col, data=data_filtered, label=col, ax=ax)
            else:
                for col in option1:
                    sns.lineplot(x='Date', y=col, data=data_filtered, label=col, ax=ax)


            date = event_date.loc[event_date['Event'] == option2, 'Date'].iloc[0]

            plt.axvline(date, color='red', linestyle='--', label='Event Date')

            plt.xlim(date - pd.Timedelta(days=20), date + pd.Timedelta(days=20))

            # set x-axis ticks
            xticks = [date - pd.Timedelta(days=20), date, date + pd.Timedelta(days = 3),date + pd.Timedelta(days = 10), date + pd.Timedelta(days=20)]
            xticklabels = ['t-20', date.strftime('%Y-%m-%d'), "t+3", "t+10", 't+20']
            plt.xticks(xticks, xticklabels)
            plt.xticks(rotation=45)

            # add title and axis labels
            plt.title('Cumulative Returns by Industry')
            plt.xlabel('Date')
            plt.ylabel('Cumulative Return')

            # move the legend to the bottom right corner
            plt.legend(loc='upper left')

            ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))


            # show the plot
            st.pyplot(fig)

        else:
            st.image(img, caption='Sunrise by the mountains')

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
                        ret20_value = row['ret20'] * 100
                        ret20_color = 'red' if ret20_value < 0 else 'green'
                        ret20_str = f"{ret20_value:.2f}%"
                        ret20_display = f"% difference t+20: <span style='color:{ret20_color};'>{ret20_str}</span>"
                        box_content.append(ret20_display)
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
                        ret20_value = row['ret20'] * 100
                        ret20_color = 'red' if ret20_value < 0 else 'green'
                        ret20_str = f"{ret20_value:.2f}%"
                        ret20_display = f"% difference t+20: <span style='color:{ret20_color};'>{ret20_str}</span>"
                        box_content.append(ret20_display)

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
                "Amid the chaos of the opening hours of the war, rumors started to swirl about Ukraine’s leadership fleeing the country. Ukrainian President Volodymyr Zelensky and his team reacted by filming a video of themselves in central Kyiv, reassuring the nation. “We are all here defending our independence, our state and it will remain so. Glory to our defenders! Glory to our women defenders! Glory to Ukraine!” Zelensky said. The president had refused a US offer to evacuate, according to the Ukrainian government, saying: “I need ammunition, not a ride.”"
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
                    "As the refugee crisis in Poland grows as hundreds of thousands are forced from their homes, the following occured to each of the industry sectors. The metal sector experienced 3.81% growth at t+3, likely driven by increased demand and regional uncertainty. Transport returns initially declined by 4.64% at t+3 due to disrupted logistics and increased fuel costs. The energy sector saw an 11.34% increase at t+3, attributed to potential supply disruptions and heightened demand. Food returns grew by 2.12% at t+3, driven by the increased demand to meet the needs of the refugee population. Lastly, the semiconductor sector returns declined by 5.63% at t+3, possibly due to supply chain disruptions and broader market uncertainty."
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
                    "Following the Irpin Bridge Evacuation, metal returns saw a moderate growth of 2.45% at t+3, possibly influenced by regional uncertainty and increased demand for resources. Transport sector experienced a 3.86% increase at t+3, likely due to heightened demand for evacuation and relocation services. Energy returns grew by 1.61% at t+3, reflecting the impact of localized disruptions and fluctuating demand. Food sector returns declined by 4.28% at t+3, potentially driven by supply chain disruptions and increased production costs in the conflict area. Lastly, Semiconductor returns increased by 2.93% at t+3, which could be an outcome of broader market dynamics rather than a direct link to the event."
            elif option2 == "Mariupol Hospital Attack":
                """
                ## Mariupol Hospital Attack
                ##### March 9, 2022
                """
                "A maternity hospital in the southeastern city of Mariupol was hit by a Russian missile. The attack came despite Russia agreeing to a 12-hour pause in hostilities to allow refugees to evacuate. A photo of a pregnant woman injured in the bombing being carried on a stretcher outside the devastated hospital became emblematic of Russia’s senseless aggression against its neighbor."
                if all_option1 in option1:
                    """
                    ## Analysis:
                    """
                    "Following Mariupol Hospital Attack."
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
            elif option2 == "Sunking of Russian main ship":
                """
                ## Sunking of Russian main ship
                ##### April 14, 2022
                """
                "Moskva, the flagship of Russia’s Black Sea fleet, sank on April 14. The cause remains disputed. Ukraine said it hit the Moskva with anti-ship cruise missiles, sparking a fire that detonated stored ammunition. Russia blamed a fire of unknown origin. Whatever the reason, the loss of the guided-missile cruiser was a major military embarrassment for Russia and its biggest wartime loss of a naval ship in 40 years."
            elif option2 == "Mariupol Steel Plant Defence":
                """
                ## Mariupol Steel Plant Defence
                ##### May 17, 2022
                """
                "The sprawling Azovstal steel plant in Mariupol became another symbol of Ukrainian resistance in the face of a much larger enemy. Defenders of the plant withstood weeks of relentless Russian bombardment before finally surrendering in May. Ukrainian officials praised the fighters, saying their fierce defense of the complex had stalled Russian forces and prevented the capture of Zaporizhzhia, further west."
            elif option2 == "Russian retreat from Kharkiv":
                """
                ## Russian retreat from Kharkiv
                ##### September 1, 2022
                """
                "A blistering Ukrainian counteroffensive in eastern Ukraine in September recaptured large swaths of territory and forced Russian troops to flee the Kharkiv region. Moscow tried to spin the hasty withdrawal as “regrouping.” But in a sign of just how badly things were going for Russia, the military was publicly criticized by a number of high-profile Kremlin loyalists including Chechen leader Ramzan Kadyrov, who supplied thousands of fighters to the offensive."
            elif option2 == "Russia starts mobilization":
                """
                ## Russia starts mobilization
                ##### September 21, 2022
                """
                "Following a string of embarrassing defeats in Ukraine, Putin announced Russia’s first mobilization since World War II on September 21. The controversial draft sparked protests — a rare sight in Russia — and an exodus of men of fighting age from the country. The partial mobilization was beset by errors and produced fighters that were poorly equipped and largely untrained. However, it significantly increased Russia’s troop numbers."
            elif option2 == "Crimea Bridge Attack":
                """
                ## Crimea Bridge Attack
                ##### October 8, 2022
                """
                "In another major blow to Moscow, the only bridge connecting Russia with the Crimean Peninsula was severely damaged by an explosion. The Kerch Strait road-and-rail bridge is both strategically important and hugely symbolic. It was opened by Putin in 2018, four years after Russia illegally annexed Crimea from Ukraine."
            elif option2 == "Kyiv Blackout":
                """
                ## Kyiv Blackout
                ##### October 10, 2022
                """
                "A new phase of the war began when Russia launched the first of several waves of missile strikes on Ukraine’s critical energy infrastructure. Using missiles, artillery shells and Iranian-made drones, Moscow began targeting Ukrainian power facilities, leaving large areas of the country without power and water."
            elif option2 == "Kherson city liberation":
                """
                ## Kherson city liberation
                ##### November 12, 2022
                """
                "After eight months of brutal Russian occupation, the southern city of Kherson was liberated on November 12, prompting scenes of celebration by residents. Russia’s hasty withdrawal from the west bank of the Dnipro River was another bleak moment for Moscow, since Kherson was the only Ukrainian regional capital that Russian forces had captured. Putin himself had formally declared Kherson to be Russian territory just weeks before his troops’ retreat."
            elif option2 == "Zelensky visits White House":
                """
                ## Zelensky visits White House
                ##### December 21, 2022
                """
                "On December 21, Zelensky traveled to Washington, DC to meet with US President Joe Biden at the White House and to address the US Congress. It was a historic and consequential visit, the first foreign trip Zelensky had made since Russia launched its invasion. Just ahead of Zelensky’s arrival, the Biden administration announced it was sending nearly $2 billion in additional security assistance to Ukraine — including a sophisticated new Patriot air defense system."
            elif option2 == "Germany sends tanks":
                """
                ## Germany sends tanks
                ##### January 25, 2023
                """
                "After weeks of geopolitical squabbling, a major moment arrived on January 25 when Germany announced it would provide Leopard 2 tanks to Kyiv and allow other European countries to export the German-made battle tank. At the same time, Biden said the US would send 31 M1 Abrams tanks to Ukraine. The move was hailed as a breakthrough in the West’s military support for Ukraine and signaled a bullish view in the West about Ukraine’s ability to reclaim occupied territory."
            elif option2 == "Biden visits Kyiv":
                """
                ## Biden visits Kyiv
                ##### February 20, 2023
                """
                "Biden made a highly symbolic surprise visit to Kyiv on February 20, his first since Russia’s full-scale invasion. Standing alongside Zelensky, the US president recalled how the pair spoke by phone as Russian forces rolled in. “One year later, Kyiv stands. And Ukraine stands. Democracy stands,” Biden declared. “The Americans stand with you and the world stands with you.” Zelensky said Biden’s visit brought Ukraine “closer to victory.” The two leaders went on a walkabout in Kyiv just as air raid sirens sounded across the city."


    elif page == "Analysis":
        st.title("Analysis")
        st.write("Add your analysis here.")

if __name__ == "__main__":
    main()


