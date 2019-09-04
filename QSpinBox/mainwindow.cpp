#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QTimer>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QTimer *timer = new QTimer(this);

    timer->setInterval(100);
    connect(timer, &QTimer::timeout, this, &MainWindow::onTimeOut);
    timer->start();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::onTimeOut()
{
    int value = ui->progressBar->value();
    if(value>=100){
        return;
    }
    value+=1;
    ui->progressBar->setValue(value);
}
