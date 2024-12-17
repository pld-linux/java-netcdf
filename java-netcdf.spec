# TODO: remove (at least some) external packages from jars and use system ones
Summary:	NetCDF Java libraries
Summary(pl.UTF-8):	Biblioteki NetCDF dla języka Java
Name:		java-netcdf
Version:	5.6.0
Release:	1
License:	BSD-like
Group:		Libraries
# download from: https://artifacts.unidata.ucar.edu/service/rest/repository/browse/downloads-netcdf-java/
Source0:	https://artifacts.unidata.ucar.edu/repository/downloads-netcdf-java/%{version}/ncIdv-%{version}.jar
# Source0-md5:	ee0140f5c68f54a0ece3b57ef670a2c0
Source1:	https://artifacts.unidata.ucar.edu/repository/downloads-netcdf-java/%{version}/netcdfAll-%{version}.jar
# Source1-md5:	be0dc55e86861adf40d1937d98ea8491
Source2:	https://artifacts.unidata.ucar.edu/repository/downloads-netcdf-java/%{version}/toolsUI-%{version}.jar
# Source2-md5:	f374af5e0772c4b12903068b17d94c47
URL:		https://www.unidata.ucar.edu/software/netcdf-java/
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The NetCDF Java library implements the Common Data Model (CDM) to
interface netCDF files and other types of scientific data formats.

%description -l pl.UTF-8
Biblioteka NetCDF Java implementuje model danych CDM (Common Data
Model) pozwalający na pracę z plikami netCDF i innymi rodzajami
formatów danych naukowych.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_javadir}
for f in ncIdv netcdfAll toolsUI ; do
	ln -sf ${f}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/${f}.jar
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/ncIdv-%{version}.jar
%{_javadir}/ncIdv.jar
%{_javadir}/netcdfAll-%{version}.jar
%{_javadir}/netcdfAll.jar
%{_javadir}/toolsUI-%{version}.jar
%{_javadir}/toolsUI.jar
