## MMM-KudaGo

Module for [MagicMirror](https://github.com/MichMich/MagicMirror). Can show upcoming events (concerts, theater plays, exhibitions and etc.), that collected from [KudaGo](https://kudago.com). 

Actual for only **Russian Federation** and **Ukraine**, because of limitations in information, provided by service. Below, in config description, is the list of available locations.

## Screenshot
![Screenshot](screenshot.jpg)


### Dependencies
* [MagicMirror](https://github.com/MichMich/MagicMirror)
* [python-shell](https://www.npmjs.com/package/python-shell)
* Python 3.6 or higher

### Installation
Navigate into your MagicMirror's modules folder
```markdown
cd ~/MagicMirror/modules
```

Clone this module repository:
```markdown
git clone https://github.com/polarbearjngl/MMM-KudaGo.git
```

Navigate to the new MMM-KudaGo folder and install the npm **python-shell** dependency
```markdown
npm install python-shell
```

Check that you have installed **Python 3.6 or higher** on your Raspberry. Just write in console `python3`, and if it exists, you will see python terminal. If not, you need to install it with this line
```markdown
sudo apt-get install python3
```

Then install required packages from requirements.txt
```markdown
sudo python3 -m pip install -r requirements.txt
```

### Configuration
Here is example of config, that must be placed in *config.js* file in array *modules*
```markdown
{
    module: 'MMM-KudaGo',               //module name
    disabled: false,                    //false if you want turn on module
    position: 'bottom_bar',             //the best is bottom
    config: {
                location: "spb",        //city for searching events. String with only one value, without comma. More info in readme.md
                categories: "concert",  //Types of events, separated by comma, that will requested from KudaGo
                days: 7                 //Number of days, for creating interval for search (since today until target days)
            }
},
```

### The following properties can be configured through config.js:

 Option | Type | Description
-------|------|-----------
`days` | Int | Number of days, for creating interval for search (since today until target days).
`nextEventInterval` | Int | Interval for changing current text. Defaults is 10 sec (`10000`).
`updateInterval` | Int | Interval for writes and reads the file. Defaults is every 6 hours (`6 * 3600 * 1000`).
`animationSpeed` | Float | Speed of text fading and changing to next. Defaults is 2.5 sec (`2.5 * 1000`).
`pythonPath` | String | Shell comand or path to Python binary. Default is `python3`.
`location` | String | City for searching events. Must be string with only one value, without comma. Possible values: <ul><li>St. Petersburg: `spb`,</li><li>Moscow: `msk`,</li><li>Novosibirsk: `nsk`,</li><li>Yekaterinburg: `ekb`,</li><li>Nizhny Novgorod: `nnv`,</li><li>Kazan: `kzn`,</li><li>Samara: `smr`,</li><li>Krasnodar: `krd`,</li><li>Sochi : `sochi`,</li><li>Ufa: `ufa`,</li><li>Krasnoyarsk: `krasnoyarsk`,</li><li>Kiev: `kev`</li></ul>
`categories` | String | Types of events, one word or separated by comma, that will requested from KudaGo. Default is `concert`. For example: <ul><li>concert</li><li>theater</li><li>party</li><li>exhibition</li><li>festival</li><li>show</li><li>games</li><li>night</li><li>evening</li><li>quest</li><li>stand_up</li><li>ball</li><li>business_events</li><li>circus</li><li>comedy_club</li><li>dance_trainings</li><li>education</li><li>entertainment</li><li>flashmob</li><li>holiday</li><li>kids</li><li>kvn</li><li>magic</li><li>masquerade</li><li>meeting</li><li>open</li><li>other</li><li>permanent_exhibitions</li><li>photo</li><li>presentation</li><li>recreation</li><li>romance</li><li>sale</li><li>social_activity</li><li>speed_dating</li><li>sport</li><li>tour</li><li>yarmarki</li><li>yoga</li></ul>
 
 All possible types of events see on [This Page](https://github.com/polarbearjngl/MMM-KudaGo/blob/b148f9b4de9ffb1098ac83b2788089c7802165d2/kudago/api/entities/event.py#L61)

