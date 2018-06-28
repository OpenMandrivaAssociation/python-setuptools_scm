Summary:	Tool to manage python package versions by scm tags
Name:		python-setuptools_scm
Version:	2.1.0
Release:	1
Group:		Development/Python
License:	MIT
Url:		https://pypi.org/project/setuptools_scm/#files
# See also	https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/e5/62/f9e1ac314464eb5945c97542acb6bf6f3381dfa5d7a658de7730c36f31a1/setuptools_scm-%{version}.tar.gz
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
python setup.py build

%install
python setup.py install --root %{buildroot}
