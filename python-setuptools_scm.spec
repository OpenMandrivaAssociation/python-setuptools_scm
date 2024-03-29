%global pypi_name setuptools_scm
%define tarname setuptools-scm

Name:           python-%{pypi_name}
Version:	7.1.0
Release:	2
Group:          Development/Python
Summary:        Tool to manage python package versions by scm tags

License:        MIT
Url:            https://pypi.org/project/setuptools_scm/#files
# See also      https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
BuildRequires:	python3dist(tomli)
# FIXME why isn't this autodetected?
Provides:	python3dist(setuptools-scm) = %{EVRD}
Provides:	python%{pyver}dist(setuptools-scm) = %{EVRD}
Requires:	python%{pyver}dist(tomli)
Requires:	python%{pyver}dist(typing-extensions)
%description
Tool to manage python package versions by scm tags

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}

%files
%doc  README.rst CHANGELOG.rst LICENSE
%{python_sitelib}/*/*
