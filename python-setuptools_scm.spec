%global pypi_name setuptools_scm
%define tarname setuptools-scm

Name:           python-%{pypi_name}
Version:	9.2.2
Release:	2
Group:          Development/Python
Summary:        Tool to manage python package versions by scm tags

License:        MIT
Url:            https://pypi.org/project/setuptools_scm/#files
# See also      https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tomli)
# FIXME why isn't this autodetected?
Provides:	python%{pyver}dist(setuptools-scm) = %{EVRD}
Requires:	python%{pyver}dist(tomli)
Requires:	python%{pyver}dist(typing-extensions)
BuildSystem:	python

%description
Tool to manage python package versions by scm tags

%files
%doc LICENSE
%{_bindir}/setuptools-scm
%{python_sitelib}/setuptools_scm
%{python_sitelib}/*.*-info
