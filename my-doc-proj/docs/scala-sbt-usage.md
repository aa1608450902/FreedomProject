### install and deploy sbt-scala

**1. sbt install**  
1. Download [sbt](https://www.scala-sbt.org/download.html) from website.  
2. Just decompression sbt-xxx.tgz and move it into `/usr/local`.  
3. Set environment variables(`SBT_HOME` and `PATH`).  
**2. sbt usage**  
Here, build a sbt-scala project to introduce the usage of sbt.
```
cd /opt && mkdir demo-pro && cd demo-pro
touch build.sbt
Enter sbt shell
$sbt:xxx> compile
$sbt:xxx> run
$sbt:xxx> package
```
**3. scala install**  
1. Download [scala](https://www.scala-lang.org/download/) from website.  
2. Just decompression scala-xxx.tgz and move it into `/usr/local`.  
3. Set environment variables(`SCALA_HOME` and `PATH`).  
**4. scala usage**  
1. Compile `scalac xxx.scala`.  
2. Run `scala -classpath . xxx.scala`