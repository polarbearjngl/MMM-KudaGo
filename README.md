## MMM-KudaGo

Module for [MagicMirror](https://github.com/MichMich/MagicMirror). Can show upcoming events (concerts, theater plays, exhibitions and etc.), that collected from [KudaGo](https://kudago.com). 

Actual for only **Russian Federation** and **Ukraine**, because of limitations in information, provided by service. Below, in config description, is the list of available locations.


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
`location` | String | City for searching events. Must be string with only one value, without comma. Possible values: <ul><li>St. Petersburg: `spb`,</li><li>Moscow: `msk`,</li><li>Novosibirsk: `nsk`,</li><li>Yekaterinburg: `ekb`,</li><li>Nizhny Novgorod: `nnv`,</li><li>Kazan: `kzn`,</li><li>Samara: `smr`,</li><li>Krasnodar: `krd`,</li><li>Sochi : `sochi`,</li><li>Ufa: `ufa`,</li><li>Krasnoyarsk: `krasnoyarsk`,</li><li>Kiev: `kev`</li></ul>
`categories` | String | Types of events, one word or separated by comma, that will requested from KudaGo. For example: <ul><li>concert</li><li>theater</li><li>exhibition</li><li>festival</li><li>stand-up</li></ul> Default is `concert`. All possible types of events see on [This Page](https://github.com/polarbearjngl/MMM-KudaGo/blob/b148f9b4de9ffb1098ac83b2788089c7802165d2/kudago/api/entities/event.py#L61)
`days` | Int | Number of days, for creating interval for search (since today until target days).
`nextEventInterval` | Int | Interval for changing current text. Defaults is 10 sec (`10000 ms`).
`updateInterval` | Int | Interval for writes and reads the file. Defaults is every 6 hours (`6 * 3600 * 1000`).
`animationSpeed` | Float | Speed of text fading and changing to next. Defaults is 2.5 sec (`2.5 * 1000`).
`pythonPath` | String | Shell comand or path to Python binary. Default is `python3`.

