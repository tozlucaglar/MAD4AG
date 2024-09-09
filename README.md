# Mobile application data for activity generation (MAD4AG)

This repository contains the scripts (src/) and libraries (lib/) for generating individuals' daily activity-travel plans from mobile phone application data. Mobile phone application data is a relatively new big data source and captures individuals' broad range of activities over multiple days with extensive population coverage, which is often challenging with conventional data collection methods. The data comprises anonymized geolocation information collected from location-enabled applications in mobile phones. Although the potential of the mobile application data is immense, it also presents significant challenges, including sampling biases, data gaps due to user inactivity, and the absence of socio-demographic variables. 

## Steps

| Step | Script/Procedure                                     | Objective                                                                                                         |
|------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 0    | `src/0-Exploratory-analysis.ipynb`                   | Perform exploratory analysis on the Mobile phone data.                                                            |
| 1    | `src/1.1-Feature-engineering-close-buildings`        | Clean and prepare the mobile phone data for further analysis.                                                     |
|      | `src/1.2-Feature-engineering-near-buildings.ipynb`   |                                                                                                                   |
|      | `src/1.3-Feature-engineering-close-buildings`        |                                                                                                                   |
| 2    | `src/2.1-Survey-data-preparation.ipynb`              | Clean and prepare the travel survey data for further analysis.                                                    |
|      | `src/2.2-Hourly-activity-frequencies.ipynb`          |                                                                                                                   |
|      | `src/2.3-Work-participation.ipynb`                   |                                                                                                                   |
|      | `src/2.4-Survey-distance_new.ipynb`                  |                                                                                                                   |
|      | `src/2.5-Survey-twins_new.ipynb`                     |                                                                                                                   |
|      | `src/2.6-Preparing-survey-twins-schedules.ipynb`     |                                                                                                                   |
| 3    | `src/3.1-Home-location-estimation.ipynb`             | Infer home and work activities from  the Mobile phone data.                                                       |
|      | `src/3.2-Work-School-location-estimation.ipynb`      |                                                                                                                   |
|      | `src/3.3-Home-Work-School-evaluation.ipynb`          |                                                                                                                   |
| 4    | `src/4-Individual-weighting_new.ipynb`               | Compute a weight for each individual in the mobile phone data.                                                    |
| 5    | `src/5.1-Preparing-MAD-for-matching.ipynb`           | Calculate matching likelihood probabilities between individuals in mobile phone and survey data.                  |
|      | `src/5.2-Matching-with-survey-twins_work_part.ipynb` |                                                                                                                   |
|      | `src/5.3-Matching-evaluation.ipynb`                  |                                                                                                                   |
| 6    | `src/6.1-Generating-multiple-days.ipynb`             | Sample survey twin travellers to bring activity-travel schedules.                                                 |
|      | `src/6.2-Multiple-days-evaluation.ipynb`             |                                                                                                                   |
| 7    | `src/7.1-Determining-other-activities.ipynb`         | Determine activity locations.                                                                                     |
| 8    | `src/8.1-Scheduling-activities-by-distance.ipynb`    | Generate multiple activity-travel plans for individuals in mobile phone data.                                     |
|      | `src/8.2-Scheduling-evaluation.ipynb`                |                                                                                                                   |
|      | `src/8.3-Scheduling-multiple-days.ipynb`             |                                                                                                                   |
| 9    | `src/9.1-Trip-distance-evaluation.ipynb`             | Evaluations and visualizations                                                                                    |
|      | `src/9.2-Visualizing-results.ipynb`                  |                                                                                                                   |

