ScanCode LicenseDB
====================

LicenseDB is likely the largest collection of software licenses available on
earth and may be beyond.

LicenseDB is a free and open database of mostly all the software licenses, in
particular all the open source software licenses, with over 2000 curated licenses
texts and their metadata.

LicenseDB is built from the ScanCode Toolkit license dataset. ScanCode Toolkit
is a leading open source code scanner and license detection engine.

LicenseDB is an essential reference license resource for license compliance and
SBOMs. LicenseDB includes all the SPDX and OSI licenses together with an extended
curated collection of other licenses and license metadata. These licenses are
carefully reviewed and curated and continusouly updated by an open community of
contributors.

LicenseDB is available as a web site, an JSON or YAML API and a git repository
making it easy to reuse and integrate in tools that need a database of reference
software licenses.


Browse
------

The web site is published at: https://scancode-licensedb.aboutcode.org/
You can search the licenses by name, key and other attributes.


API
------

The index is available at either:

- as JSON: https://scancode-licensedb.aboutcode.org/index.json
- as YAML: https://scancode-licensedb.aboutcode.org/index.yml

The index contains a list of the license keys with key metadata and links to the
license details and texts using this license key as an identifier:

- as JSON: https://scancode-licensedb.aboutcode.org/<license key>.json
  for instance: https://scancode-licensedb.aboutcode.org/gpl-2.0.json

- as YAML: https://scancode-licensedb.aboutcode.org/<license key>.yml
  for instance: https://scancode-licensedb.aboutcode.org/gpl-2.0.yml

- as text for the full license text: https://scancode-licensedb.aboutcode.org/<license key>.LICENSE 
  for instance: https://scancode-licensedb.aboutcode.org/gpl-2.0.LICENSE


Git
-----

This git repository contains the full history of the generated HTML and JSON API
documents: https://github.com/nexB/scancode-licensedb


This git repository contains the original and editable source files:
https://github.com/nexB/scancode-toolkit

- for the metadata of a license, for instance at https://github.com/nexB/scancode-toolkit/edit/develop/src/licensedcode/data/licenses/gpl-2.0.yml

- for the text of a license, for instance at https://github.com/nexB/scancode-toolkit/edit/develop/src/licensedcode/data/licenses/gpl-2.0.LICENSE


Support
--------

- Chat with us at: https://gitter.im/aboutcode-org/discuss
- Report issues or ask questions at: https://github.com/nexB/scancode-toolkit/issues and
  https://github.com/nexB/scancode-licensedb/issues
- Visit https://www.aboutcode.org/ for more open source and open data projects.


Build
-----

To re/generate the HTML and API content use this command::

    $ make build


Upgrade
-------

To upgrade to the latest scancode-toolkit and generate the HTML and API content
run this command::

    $ make clean upgrade build publish


License
-------

SPDX-License-Identifier: CC-BY-4.0 AND Apache-2.0

https://github.com/nexB/scancode-licensedb
Copyright (c) nexB Inc. and others.
ScanCode is a trademark of nexB Inc.

ScanCode LicenseDB data is licensed under the Creative Commons Attribution
License 4.0 (CC-BY-4.0).
Some licenses, such as the GNU GENERAL PUBLIC LICENSE, are subject to other licenses.
See the corresponding license text for the specific license conditions.

ScanCode LicenseDB software is licensed under the Apache License version 2.0.
You may not use this software except in compliance with the License.
You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

ScanCode LicenseDB is generated with ScanCode Toolkit. The database and its contents
are provided on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.
No content from ScanCode LicenseDB should be considered or used as legal advice.
Consult an attorney for any legal advice.

Visit https://github.com/nexB/scancode-licensedb for support.

ScanCode Toolkit is a free Software Composition Analysis tool from nexB Inc. and
others.
Visit https://github.com/nexB/scancode-toolkit for support and download.
