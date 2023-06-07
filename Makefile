# SPDX-License-Identifier: CC-BY-4.0 AND Apache-2.0
#
# https://github.com/nexB/scancode-licensedb
# Copyright (c) nexB Inc. and others.
# ScanCode is a trademark of nexB Inc.
#
# ScanCode LicenseDB data is licensed under the Creative Commons Attribution
# License 4.0 (CC-BY-4.0).
# Some licenses, such as the GNU GENERAL PUBLIC LICENSE, are subject to other licenses.
# See the corresponding license text for the specific license conditions.
#
# ScanCode LicenseDB software is licensed under the Apache License version 2.0.
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# ScanCode LicenseDB is generated with ScanCode Toolkit. The database and its contents
# are provided on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied.
# No content from ScanCode LicenseDB should be considered or used as legal advice.
# Consult an attorney for any legal advice.
#
# Visit https://github.com/nexB/scancode-licensedb for support.
#
# ScanCode Toolkit is a free Software Composition Analysis tool from nexB Inc. and
# others.
# Visit https://github.com/nexB/scancode-toolkit for support and download.

PYTHON_EXE=python3
ACTIVATE=. bin/activate;
BLACK_ARGS=--exclude="docs" .

conf:
	@echo "-> Configure the Python venv, clone and install scancode-toolkit"
	${PYTHON_EXE} -m venv venv
	@git clone https://github.com/nexB/scancode-toolkit.git
	@venv/bin/pip install --upgrade pip
	@venv/bin/pip install -e ./scancode-toolkit/
	@venv/bin/scancode-reindex-licenses

clean:
	@echo "-> Restoring the repository to a clean state"
	git clean -fd
	rm -rf scancode-toolkit/
	git restore --worktree docs/

licensedb:
	@echo "-> Generate the HTML content"
	@venv/bin/scancode-license-data --path docs/
	@echo "Available at docs/index.html"

.PHONY: conf clean licensedb
