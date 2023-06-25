
my_comments = {
    "progress" : {
        "steady" : "has made steady progress in French throughout the term.",
        "fine" : "has made encouraging progress in French throughout term.",
        "good" : "has made noticeable progress in French thanks to a diligent approach to learning.",
    },
    "module" : {
        "1" : "Our main topic on Free Time allowed him to develop his grasp of the three main tenses \nwhilst covering well-liked topics such as internet activities.",
        "2" : "Our topic of Free Time has given him the opportunity to expand his vocabulary with words related to leisure, \nas well as enabling him to develop his grasp of the three main tenses.",
        "3" : "The topic of Free Time covered in class has enabled him to add expressions such as sports and games to his word bank, \nwhilst giving him the opportunity to extend his grasp of the three main tenses."
    },
    "total" : {
        "low" : "found the Spring assessment challenging yet attempted most questions,",
        "mid" : "performed reasonably well in the Spring assessment,",
        "high" : "performed well in the Spring assessment,",
        "top" : "performed very well across all three papers of the Spring assessment,"
    },
    "reading" : {
        "low" : "displaying a growing understanding of the language and its basic grammar rules.",
        "mid" : "displaying a fairly good recollection of vocabulary and a sound knowledge of the present tense.",
        "high" : "demonstrating a good recollection of vocabulary and a growing confidence differentiating tenses.",
        "top" : "demonstrating an excellent recollection of vocabulary and fine deductive skills."
    },
    "grammar" : {
        "low" : "The grammar section showed a steady improvement of his knowledge of verbs and tenses,",
        "mid" : "In the grammar quiz, his answers showed an increase in his conjugation skills,",
        "high" : "In the first section, a grammar quiz, his answers showed a sound knowledge of verb conjugation,"
    },
    "writing" : {
        "low" : "but the writing section proved to be quite a challenge, and his sentences lacked both detail and accuracy.",
        "mid" : "and, in the writing section, his paragraph contained simple yet effective sentences in the present tense.",
        "high" : "and, in the third section, the sentences of his written paragraph were accuracy and in two different tenses.",
        "top" : "and his written paragraph in the third section contained both detail and verbs accurately conjugated in three different tenses."
    }
}

import csv
import random

with open('frenchgrades.csv') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    line_count = 0

    for row in spreadsheet:
    #Starter line, which will print line 0 with the headers
        if line_count == 0:
            print()
            print("Welcome to the Report-O-Matic!")
            print(f'Using the grades you entered into your class spreadsheet, \nit will create reports containing: {", ".join(row)}.')
            print()
            line_count += 1
        else:
        # Will print 1 full report at a time, containing:
            pupil_name = row['Name'] # Name of pupil, as per csv file
            pupil_pronoun = row['Pronoun'] # Pronoun of pupil, as per csv file
        # Process to decide progress of pupil, comparing total in first exam to total in second exam
        # that are stored in the frenchgrades.csv file
        # and using phrases from the my_comments
            spring_grade = row['Total2']
            autumn_grade = row['Total1']
            if spring_grade < autumn_grade:
                progress = my_comments['progress']['steady']
            elif spring_grade == autumn_grade:
                progress = my_comments['progress']['fine']
            else:
                progress = my_comments['progress']['good']
        # Process to randomly chose a comment from dictionary to describe the term's topic - all equivalent
            random_number = random.randint(1, 3)
            if random_number == 1:
                topic_comment = my_comments['module']['1']
            elif random_number == 2:
                topic_comment = my_comments['module']['2']
            else:
                topic_comment = my_comments['module']['3']
        # Process to determine success in exam, using the total grade in csv file and phrases from dictionary
            pupil_performance = row['Total2']
            if float(pupil_performance) >= 45.0:
                performance = my_comments['total']['top']
            elif float(pupil_performance) <= 10.0:
                performance = my_comments['total']['low']
            elif float(pupil_performance) <= 25.0:
                performance = my_comments['total']['mid']
            else:
                performance = my_comments['total']['high']
            # Process to determine success in reading section, using reading grade in csv file and phrases from dict
            pupil_read_grade = row['Read2']
            if float(pupil_read_grade) >= 4.0:
                reading = my_comments['reading']['low']
            elif float(pupil_read_grade) >= 12.0:
                reading = my_comments['reading']['mid']
            elif float(pupil_read_grade) >= 16.0:
                reading = my_comments['reading']['high']
            else:
                reading = my_comments['reading']['top']
            # Printing final report with carriage returns for clarity, initially for boys using 'his' and 'him'

            boy_text = (f'{pupil_name} {progress} \n{topic_comment} \n{pupil_pronoun} {performance} {reading}')

            from collections import OrderedDict
            def replace_all(text, dic):
                for i, j in dic.items():
                    text = text.replace(i, j)
                return text
            od = OrderedDict([("his", "her"), ("him", "her")])
            girl_text = replace_all(boy_text, od)

            if pupil_pronoun == 'He':
                final_report = boy_text
            if pupil_pronoun == 'She':
                final_report = girl_text

            print(final_report)
            print()
            saving_choice = input("Would you like to save this report into the frenchreport text file? y/n \n")
            if saving_choice == 'y':
                f = open("frenchreport.txt", "a")
                f.write(f'\nHere is the report for {pupil_name}: \n{final_report}\n')
                f.close()
            else:
                f = open("frenchreport.txt", "a")
                f.write(f"\nNo report for {pupil_name}.\n")
                f.close()


        # To move on to the next row of csv file, which will write report for next pupil
            line_count +=1