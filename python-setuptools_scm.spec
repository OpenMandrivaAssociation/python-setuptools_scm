# Created by pyp2rpm-2.0.0
%global pypi_name setuptools_scm
%define tarname setuptools-scm
%global with_python2 1

Name:           python-%{pypi_name}
Version:	5.0.1
Release:	1
Group:          Development/Python
Summary:        Tool to manage python package versions by scm tags

License:        MIT
Url:            https://pypi.org/project/setuptools_scm/#files
# See also      https://github.com/pypa/setuptools_scm
Source0:	https://files.pythonhosted.org/packages/af/df/f8aa8a78d4d29e0cffa4512e9bc223ed02f24893fe1837c6cee2749ebd67/setuptools_scm-5.0.1.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools
%endif # if with_python2

# FIXME why isn't this autodetected?
Provides:	python3dist(setuptools-scm)


%description
Tool to manage python package versions by scm tags


%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        Tool to manage python package versions by scm tags 
# FIXME why isn't this autodetected?
Provides:	python2dist(setuptools-scm)

%description -n python2-%{pypi_name}
Tool to manage python package versions by scm tags

%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2

%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc  README.rst CHANGELOG.rst LICENSE
%{python_sitelib}/*/*
#%%{python_sitelib}/pep8.py

%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  README.rst CHANGELOG.rst LICENSE
%{python2_sitelib}/*/*
#%%{python2_sitelib}/pep8.*
%endif # with_python2
