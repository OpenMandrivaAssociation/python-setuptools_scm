%define module setuptools-scm
%define oname setuptools_scm

Name:		python-setuptools_scm
Summary:	Tool to manage python package versions by scm tags
Version:	10.0.5
Release:	1
Group:		Development/Python
License:	MIT
# See also https://github.com/pypa/setuptools_scm
URL:		https://pypi.org/project/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/source/s/%{oname}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tomli)
BuildRequires:	python%{pyver}dist(vcs-versioning)
BuildRequires:	python%{pyver}dist(wheel)
# keep provides for package compatibility re setuptools_scm
Provides:	python%{pyver}dist(setuptools_scm) = %{EVRD}

%description
Tool to manage python package versions by scm tags.

%files
%{_bindir}/%{module}
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
