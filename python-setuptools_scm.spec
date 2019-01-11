Summary:	Tool to manage python package versions by scm tags
Name:		python-setuptools_scm
Version:	3.1.0
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/setuptools_scm/#files
# See also	https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildArch:	noarch

%description
Tool to manage python package versions by scm tags

%files
%{py_puresitedir}/setuptools_scm*

%prep
%autosetup -p1 -n setuptools_scm-%{version}

%build
%py_build

%install
python setup.py install --root %{buildroot}
