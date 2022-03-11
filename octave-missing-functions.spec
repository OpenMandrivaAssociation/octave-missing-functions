%define octpkg missing-functions

Summary:	Find functions that are in Matlab but not in Octave
Name:		octave-%{octpkg}
Version:	1.0.2
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Find functions that are in Matlab but not in Octave.

This package is part of unmantained Octave-Forge collection.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

