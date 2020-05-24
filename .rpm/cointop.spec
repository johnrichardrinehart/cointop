%define version     1.4.6
%global commit      69391a7c6f3a920c175685b9917086d449f4c1ff72c5b98ab08118489f15c0a9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           cointop
Version:        %{version}
Release:        6%{?dist}
Summary:        Terminal based application for tracking cryptocurrencies
License:        Apache-2.0
URL:            https://cointop.sh
Source0:        https://github.com/miguelmota/%{cointop}/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  golang >= 1.13

%description
cointop is a fast and lightweight interactive terminal based UI application for tracking and monitoring cryptocurrency coin stats in real-time.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir -p ./_build/src/github.com/miguelmota
ln -s $(pwd) ./_build/src/github.com/miguelmota/%{name}

export GOPATH=$(pwd)/_build:%{gopath}
GO111MODULE=off go build -ldflags="-linkmode=external -compressdwarf=false -X github.com/miguelmota/cointop/cointop.version=%{version}" -o x .

%install
install -d %{buildroot}%{_bindir}
install -p -m 0755 ./x %{buildroot}%{_bindir}/%{name}

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
