from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request):
        context = {}
        return render(request, 'main_module/index.html', context)


class DownloadView(View):
    def get(self, request):
        import wget

        url = "https://dl1.freeserver.top/m3/film/1402/04/Absolutely.Anything.2015.480p.BluRay.HardSub.DigiMoviez.mp4"

        import sys
        import requests

        link = url
        file_name = "/home/amir/testMovieService/static/video/video.mp4"
        with open(file_name, "wb") as f:
            print("Downloading %s" % file_name)
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()
        return HttpResponse("okab")
