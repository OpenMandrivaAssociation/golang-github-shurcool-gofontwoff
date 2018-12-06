# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/gofontwoff
%global commit          29b52fc0a18d8e3a04d56ae2401154eeed67b029

%global common_description %{expand:
Package gofontwoff provides the Go font family in Web Open Font Format.

It's a Go package that statically embeds Go font family WOFF data, exposing 
it via an http.FileSystem.

These fonts were created by the Bigelow & Holmes foundry specifically for 
the Go project. See https://blog.golang.org/go-fonts for details.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Go font family in Web Open Font Format
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git29b52fc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180417git29b52fc
- First package for Fedora

