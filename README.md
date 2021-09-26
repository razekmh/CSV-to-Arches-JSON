<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** razekmh, CSV-to-Arches-JSON, data_champ, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://github.com/razekmh/CSV-to-Arches-JSON">
    <img src="images/logo.png" alt="Logo" width="%80" height="%80">
  </a>

  <h3 align="center">CSV-to-Arches-JSON</h3>

  <p align="center">
    Converts CSV files to JSON files readable by Arches system
    <br />
```diff
    - THIS PROJECT IS STILL UNDER DEVELOPMENT
```
 <br />
    please check the <a href="#roadmap">roadmap</a> for a full view of the develpment timeline <br />
    <a href="https://github.com/razekmh/CSV-to-Arches-JSON"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/razekmh/CSV-to-Arches-JSON/issues">Report Bug</a>
    ·
    <a href="https://github.com/razekmh/CSV-to-Arches-JSON/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This will be a utility to transform CSV of a specified format to JSON format readable by Arches.

_"[Arches](https://arches.readthedocs.io/en/latest/) is a web-based, geospatial information system for cultural heritage inventory and management. The platform is purpose-built for the international cultural heritage field, and it is designed to record all types of immovable heritage, including archaeological sites, buildings and other historic structures, landscapes, and heritage ensembles or districts."_

Data input to Arches can be achieved using a dedicated GUI or an API. Bulk data upload is only possible using the API. [Arches API accepts data in three formats](https://arches.readthedocs.io/en/latest/import-export/); JSON, CSV and shapefiles. Each of the formats require a dedicated structure. 

Arches main data structure is based on [resource models](https://arches.readthedocs.io/en/latest/data-model/#resource-model-overview). A resource model must be created before its data is added to the system. Multiple resource models can be created for any project and relationships between them can be established. 

The underlying design of the resource models is based on JSON objects. This allows any resource model to encode cascading attributes with multiple instances at any level. The transformation between this tree-shaped JSON and the flat CSV is the main issue this repo is trying to tackle.   

The structure (and all config info) of an Arches' resource model can be exported in JSON. An example of the resource model export file is [here](https://github.com/razekmh/CSV-to-Arches-JSON/blob/main/Activity%20Resource%20Model.json). The attributes within the JSON object in the file describe the resource model structure as well as its visualization attributes.  

---
#### CSV and shapefile upload: 
Assuming that you are using the API to input data to Arches, you will need a mapping file for each resource model. You can download the mapping file from the _Arches designer_ page. A mapping file for _Example resource file_ looks like this.
```JSON
{
    "resource_model_id": "f2a47ff0-c4cb-4914-9e19-da7142eaf29d",
    "resource_model_name": "Example Resource Model",
    "nodes": [
        {
            "arches_nodeid": "205ee073-1d93-4119-ad5f-8b830be005aa",
            "arches_node_name": "Name",
            "file_field_name": "",
            "data_type": "string",
            "export": true
        },
        {
            "arches_nodeid": "b69e5110-95f2-46dc-8243-6b1297cf969e",
            "arches_node_name": "Active",
            "file_field_name": "",
            "data_type": "boolean",
            "export": true
        },
        {
            "arches_nodeid": "54e8646e-dd42-4c52-a392-3eeb2d6f6345",
            "arches_node_name": "Type",
            "file_field_name": "",
            "data_type": "concept",
            "concept_export_value": "label",
            "export": true
        }
    ]
}
```
To upload a CSV file, the mapping file should be edited to match the _file_field_name_ attribute with the respective column names in the CSV or shapefile file. 

more details about uploading the CSV file is available [here](https://arches.readthedocs.io/en/latest/import-export/#csv-file-requirements). You will see in the documentation page that only one level of cascading is allowed in the CSV format. This means that for an attribute such as _name_, you can include "children attributes" such as _name type_ and _name value_. However adding additional levels will confuse the system. Additionally, Arches sometimes gets confused by only one level. The behaviour of the CSV upload function seems to be unstable. 

---
#### JSON upload:
[JSON upload is not recommended](https://arches.readthedocs.io/en/latest/import-export/#json-import) due to its complexity. The design of Arches JSON can be found in the [same page](https://arches.readthedocs.io/en/latest/import-export/#json-import)

### Built With

* [Python3.8](https://www.python.org/downloads/release/python-380/)
* JSON, CSV, UUID

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/razekmh/CSV-to-Arches-JSON.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/razekmh/CSV-to-Arches-JSON/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Mahmoud Abdelrazek - [@data_champ](https://twitter.com/data_champ)

Project Link: [https://github.com/razekmh/CSV-to-Arches-JSON](https://github.com/razekmh/CSV-to-Arches-JSON)



<!-- ACKNOWLEDGEMENTS -->
<!-- ## Acknowledgements
* []()
* []()
* []()
-->




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/razekmh/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/razekmh/CSV-to-Arches-JSON/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/razekmh/repo.svg?style=for-the-badge
[forks-url]: https://github.com/razekmh/CSV-to-Arches-JSON/network/members
[stars-shield]: https://img.shields.io/github/stars/razekmh/repo.svg?style=for-the-badge
[stars-url]: https://github.com/razekmh/CSV-to-Arches-JSON/stargazers
[issues-shield]: https://img.shields.io/github/issues/razekmh/repo.svg?style=for-the-badge
[issues-url]: https://github.com/razekmh/CSV-to-Arches-JSON/issues
[license-shield]: https://img.shields.io/github/license/razekmh/repo.svg?style=for-the-badge
[license-url]: https://github.com/razekmh/CSV-to-Arches-JSON/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/razekmh
