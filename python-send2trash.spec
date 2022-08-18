# Created by pyp2rpm-3.3.3
%bcond_without tests
%global pypi_name Send2Trash
%define psnme Send2Trash 

Name:           python-%{pypi_name}
Version:        1.5.0
Release:        2
Summary:        Serialization based on ast.literal_eval

License:        MIT
URL:            https://github.com/arsenetar/send2trash
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:	fdupes

%if %{with tests}
BuildRequires:  python-attrs
BuildRequires:  python-pytz
%endif

Requires:	python-gobject3

%description
Send2Trash is a small package that sends files to the Trash (or Recycle Bin) *natively* and on
*all platforms*. On OS X, it uses native ``FSMoveObjectToTrashSync`` Cocoa calls, on Windows, it
uses native (and ugly) ``SHFileOperation`` win32 calls. On other platforms, if `PyGObject`_ and
`GIO`_ are available, it will use this.  Otherwise, it will fallback to its own implementation
of the `trash specifications from freedesktop.org`_.

%{?python_provide:%python_provide python-%{pypi_name}}

%prep
%setup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
#python setup.py build
%py3_build

%install
%py3_install
#python setup.py install

%if %{with tests}
%check
%{__python3} setup.py test
%endif


%files -n python-%{pypi_name}
%license LICENSE
%doc CHANGES.rst
%{python3_sitelib}/*
#%%{python3_sitelib}/__pycache__/*
#%%{python3_sitelib}/%{pypi_name}.py
#%%{python3_sitelib}/%{pypi_name}
#%%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

