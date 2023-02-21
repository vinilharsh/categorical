from distutils.core import setup
setup(
  name = 'categorical',         # How you named your package folder (MyLib)
  packages = ['categorical'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Statistical data visualization',   # Give a short description about your library
  author = 'Vinil Harsh',                   # Type in your name
  author_email = 'vinilharsh123@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/categorical',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          "numpy>=1.20,!=1.24.0",
    "pandas>=1.2",
    "matplotlib>=3.3,!=3.6.1",
    "python >=3.8",
      ],
  classifiers=[
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "License :: OSI Approved :: BSD License",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Multimedia :: Graphics",
    "Operating System :: OS Independent",
    "Framework :: Seaborn",

  ],
)