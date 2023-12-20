#include <cpr/cpr.h>
#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <Eigen/Dense>
#include <string>
#include <chrono>
using std::string;

using json = nlohmann::json;
using Eigen::MatrixXf;
using Eigen::VectorXf;
using namespace std::chrono;

class Task
{
public:
    Task(string url)
    {
        cpr::Response r = cpr::Get(cpr::Url{url});
        r.status_code;                  // 200
        r.header["content-type"];       // application/json; charset=utf-8
        r.text;                         // JSON text string
        if (r.status_code == 200) {
            json donnees = json::parse(r.text);
            identifier = donnees["identifier"];
            size = donnees["size"];
            a.resize(size, size);
            b.resize(size);
            x.resize(size);
            for (int i = 0; i < size; ++i) {
                for (int j = 0; j < size; ++j) {
                    a(i, j) = donnees["a"][i][j];
                }
            }
            for (int i = 0; i < size; ++i) {
                b(i) = donnees["b"][i];
            }
            time = donnees["time"];
        } else {
            std::cout << "Failed to get response, status code: " << r.status_code << std::endl;
        }
    }

    void work()
    {
        auto start_time = high_resolution_clock::now();
        // x = a.colPivHouseholderQr().solve(b); // Environ 13.2 secondes pour une taille de 4000
        x = a.lu().solve(b); // Environ 1.9 secondes pour une taille de 4000
        auto end_time = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(end_time - start_time);
        std::cout << "Duration: " << duration.count() << " milliseconds" << std::endl;
    }

private:
    int identifier;
    int size;
    MatrixXf a;
    VectorXf b;
    float time;
    VectorXf x;
};


int main(int argc, char** argv) {
    Task t = Task("http://localhost:8000");
    t.work();
    return 0;
}