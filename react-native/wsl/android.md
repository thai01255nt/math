sudo apt install unzip
wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip -d Android
rm platform-tools-latest-linux.zip
sudo apt install -y lib32z1 openjdk-8-jrk
set -gx JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
set -gx PATH $JAVA_HOME/bin $PATH
cd /Android/tools/bin
./sdkmanager "platform-tools" "platforms;android-26" "build-tools;26.0.3"
set -gx ANDROID_HOME ~/Android/
set -gx PATH $ANDROID_HOME/tools
set -gx PATH $ANDROID_HOME/platform-tools
android update sdk --no-ui
sudo apt-get install gradle
gradle -v

set -gx ANDROID_HOME ~/android_sdk/cmdline-tools/latest
set -gx PATH $ANDROID_HOME/bin $PATH
set -gx PATH $ANDROID_HOME/lib $PATH
