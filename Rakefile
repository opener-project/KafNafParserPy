require 'rake/clean'

LIB_NAME           = 'KafNafParserPy'
UPSTREAM_DIRECTORY = "upstream/#{LIB_NAME}-master"

UPSTREAM_FILES = [
  'README.md',
  'LICENSE',
  'naf.dtd',
  'naf_example.xml',
  'kaf_example.xml'
]

CLEAN.include('upstream', 'build', 'dist', 'MANIFEST')

directory 'upstream' do |task|
  sh "wget https://github.com/cltl/#{LIB_NAME}/archive/master.zip"
  sh "unzip master.zip -d #{task.name}"
  sh 'rm master.zip'
end

directory LIB_NAME do |task|
  sh "rm -rf #{LIB_NAME}"
  sh "mv #{UPSTREAM_DIRECTORY} #{task.name}"
end

UPSTREAM_FILES.each do |file|
  file(file) do |task|
    sh "mv #{UPSTREAM_DIRECTORY}/#{task.name} #{task.name}"
  end
end

desc 'Syncs with the upstream package'
task :sync => ['upstream'] + UPSTREAM_FILES + [LIB_NAME, 'clean']

desc 'Builds the Python package'
task :package do
  sh 'python setup.py sdist'
end
