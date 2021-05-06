/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionNovo;
    QAction *actionAbrir;
    QAction *actionSalvar;
    QWidget *centralWidget;
    QTextEdit *textEdit;
    QMenuBar *menuBar;
    QMenu *menuArquivo;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(400, 300);
        actionNovo = new QAction(MainWindow);
        actionNovo->setObjectName(QString::fromUtf8("actionNovo"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icones/1159633.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionNovo->setIcon(icon);
        actionAbrir = new QAction(MainWindow);
        actionAbrir->setObjectName(QString::fromUtf8("actionAbrir"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icones/open-in-popup.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionAbrir->setIcon(icon1);
        actionSalvar = new QAction(MainWindow);
        actionSalvar->setObjectName(QString::fromUtf8("actionSalvar"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icones/download.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionSalvar->setIcon(icon2);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        textEdit = new QTextEdit(centralWidget);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setGeometry(QRect(0, 0, 401, 221));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 400, 22));
        menuArquivo = new QMenu(menuBar);
        menuArquivo->setObjectName(QString::fromUtf8("menuArquivo"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuArquivo->menuAction());
        menuArquivo->addSeparator();
        menuArquivo->addAction(actionNovo);
        menuArquivo->addSeparator();
        menuArquivo->addAction(actionAbrir);
        menuArquivo->addSeparator();
        menuArquivo->addAction(actionSalvar);
        mainToolBar->addAction(actionNovo);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionAbrir);
        mainToolBar->addSeparator();
        mainToolBar->addAction(actionSalvar);
        mainToolBar->addSeparator();

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        actionNovo->setText(QApplication::translate("MainWindow", "Novo", nullptr));
        actionAbrir->setText(QApplication::translate("MainWindow", "Abrir", nullptr));
        actionSalvar->setText(QApplication::translate("MainWindow", "Salvar", nullptr));
        menuArquivo->setTitle(QApplication::translate("MainWindow", "Arquivo", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
